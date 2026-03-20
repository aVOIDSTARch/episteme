import { useEffect, useState } from 'react'
import './App.css'

type FileNode = {
  path: string
  name: string
  type: string
  size: number
  modified_at: number
}

type FileContent = {
  path: string
  content: string
  type: string
  size: number
  metadata: Record<string, any> | null
}

function App() {
  const [nodes, setNodes] = useState<FileNode[]>([])
  const [selected, setSelected] = useState<string>('')
  const [content, setContent] = useState<FileContent | null>(null)
  const [query, setQuery] = useState('')
  const [searchResults, setSearchResults] = useState<FileNode[]>([])

  useEffect(() => {
    fetch('/api/v1/framework/tree')
      .then(r => r.json())
      .then(setNodes)
  }, [])

  const loadFile = (path: string) => {
    setSelected(path)
    fetch(`/api/v1/framework/file?path=${encodeURIComponent(path)}`)
      .then(r => r.json())
      .then(setContent)
      .catch(() => setContent(null))
  }

  const runSearch = () => {
    if (!query) return
    fetch(`/api/v1/framework/search?query=${encodeURIComponent(query)}`)
      .then(r => r.json())
      .then((results: any[]) => setSearchResults(results))
  }

  return (
    <div className="app-shell">
      <header className="app-header">
        <div>
          <h1>Episteme Knowledge Interface</h1>
          <p>Browse, search, and annotate your episteme-framework files.</p>
        </div>
      </header>

      <section className="controls">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search across framework files..."
        />
        <button onClick={runSearch}>Search</button>
      </section>

      <div className="main-grid">
        <aside className="panel">
          <h2>File Explorer</h2>
          {nodes.length === 0 ? (
            <p>Loading files...</p>
          ) : (
            <ul>
              {nodes.map((n) => (
                <li key={n.path}>
                  <button className="link-button" onClick={() => loadFile(n.path)}>{n.name} ({n.type})</button>
                </li>
              ))}
            </ul>
          )}
        </aside>

        <article className="panel">
          <h2>File Viewer</h2>
          {selected ? <p>Selected: <strong>{selected}</strong></p> : <p>Select a file</p>}
          {content ? <pre>{content.content}</pre> : <p>No file loaded.</p>}
        </article>

        <aside className="panel">
          <h2>Search Results</h2>
          {searchResults.length === 0 ? <p>No search results</p> : (
            <ul>{searchResults.map((r) => <li key={r.path}>{r.path}</li>)}</ul>
          )}
        </aside>
      </div>
    </div>
  )
}

export default App

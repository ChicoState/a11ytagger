import { BrowserRouter, Routes, Route, useLocation } from 'react-router-dom'
import { Navbar } from 'src/components/Navbar'
import { Home } from 'src/components/Home'
import { Upload } from 'src/components/Upload'

function AppContent() {
  const location = useLocation()

  return (
    <div className="min-h-screen" style={{ backgroundColor: 'var(--bg-color)' }}>
      <Navbar currentPath={location.pathname} />
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/upload/" element={<Upload />} />
        <Route path="/faq/" element={<div className="p-8"><h1 className="text-4xl font-bold">FAQ</h1></div>} />
        <Route path="/about/" element={<div className="p-8"><h1 className="text-4xl font-bold">About</h1></div>} />
      </Routes>
    </div>
  )
}

function App() {
  return (
    <BrowserRouter>
      <AppContent />
    </BrowserRouter>
  )
}

export default App

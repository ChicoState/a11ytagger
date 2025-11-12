import { useState } from 'react'
import type { ReactNode } from 'react'
import { ChevronRight } from 'lucide-react'

interface ToolProps {
  title: string
  children: ReactNode
  defaultOpen?: boolean
}

export function Tool({ title, children, defaultOpen = false }: ToolProps) {
  const [isOpen, setIsOpen] = useState(defaultOpen)

  return (
    <div className="tool-foldout">
      <button
        type="button"
        className="tool-header"
        onClick={() => setIsOpen(!isOpen)}
        aria-expanded={isOpen}
      >
        <span className="tool-title">{title}</span>
        <ChevronRight
          className={`tool-chevron ${isOpen ? 'rotated' : ''}`}
          size={16}
        />
      </button>
      <div className={`tool-content ${isOpen ? 'expanded' : ''}`}>
        <div className="tool-content-inner">
          {children}
        </div>
      </div>

      <style>{`
        .tool-foldout {
          margin-bottom: 0.5rem;
        }

        .tool-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          width: 100%;
          padding: 0.75rem 1rem;
          background: #e6e6e6;
          border: 1px solid #ccc;
          border-radius: 4px;
          cursor: pointer;
          transition: background-color 0.2s;
          user-select: none;
        }

        .tool-header:hover {
          background: #d9d9d9;
        }

        .tool-header:focus {
          outline: 2px solid #666;
          outline-offset: 2px;
        }

        .tool-title {
          font-weight: 600;
          font-size: 1rem;
          color: #333;
        }

        .tool-chevron {
          transition: transform 0.3s ease;
          flex-shrink: 0;
        }

        .tool-chevron.rotated {
          transform: rotate(90deg);
        }

        .tool-content {
          max-height: 0;
          overflow: hidden;
          transition: max-height 0.3s ease;
        }

        .tool-content.expanded {
          max-height: 10000px;
        }

        .tool-content-inner {
          padding: 1rem;
          background: white;
          border: 1px solid #ddd;
          border-top: none;
          border-radius: 0 0 4px 4px;
        }
      `}</style>
    </div>
  )
}

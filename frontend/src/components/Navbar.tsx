import { useState } from 'react'
import { Link } from 'react-router-dom'
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
} from 'src/components/ui/navigation-menu'
import { SidebarTrigger } from './ui/sidebar'

interface NavbarProps {
  onSidebarToggle?: () => void
  currentPath?: string
}

export function Navbar({ onSidebarToggle, currentPath = '/' }: NavbarProps) {
  const [sidebarExpanded, setSidebarExpanded] = useState(true)

  const handleSidebarToggle = () => {
    setSidebarExpanded(!sidebarExpanded)
    onSidebarToggle?.()
  }

  const navLinks = [
    { href: '/', label: 'Home' },
    { href: '/upload/', label: 'Upload PDF' },
    { href: '/faq/', label: 'FAQ' },
    { href: 'https://github.com/ChicoState/a11ytagger', label: 'Github', external: true },
    { href: '/about/', label: 'About' },
  ]

  return (
    <nav className="sticky top-0 z-50 bg-[var(--navbar-color)] px-5 py-2.5 flex justify-between items-center">
      <div className="flex items-center gap-5 pl-0">
        <NavigationMenu viewport={false}>
          <NavigationMenuList className="gap-5">
            {navLinks.map((link) => (
              <NavigationMenuItem key={link.href}>
                {link.external ? (
                  <NavigationMenuLink
                    href={link.href}
                    active={currentPath === link.href}
                    className="nav-link"
                    target="_blank"
                    rel="noopener noreferrer"
                  >
                    {link.label}
                  </NavigationMenuLink>
                ) : (
                  <NavigationMenuLink asChild active={currentPath === link.href} className="nav-link">
                    <Link to={link.href}>{link.label}</Link>
                  </NavigationMenuLink>
                )}
              </NavigationMenuItem>
            ))}
          </NavigationMenuList>
        </NavigationMenu>
      </div>

      <button type="button" className="settings-btn" title="Settings" aria-label="Settings">
        <img src="/assets/icon-gear.svg" width="25" height="25" alt="Settings" />
      </button>

      <style>{`
        .nav-link {
          background-color: var(--btn-color) !important;
          color: var(--text-color) !important;
          text-decoration: none;
          padding: 10px 20px !important;
          border-radius: 4px;
          font-size: 16px;
          transition: background-color 0.3s;
          cursor: pointer;
          display: inline-block;
          height: auto !important;
          min-height: auto !important;
        }

        .nav-link:hover {
          background-color: var(--btn-hover-color) !important;
        }

        .nav-link:focus {
          outline: 2px solid var(--btn-focus-color) !important;
          outline-offset: 2px;
          box-shadow: none !important;
        }

        .nav-link[data-active="true"] {
          background-color: var(--btn-selected-color) !important;
        }

        .settings-btn {
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 10px;
          background-color: var(--btn-color);
          border: none;
          border-radius: 4px;
          width: 40px;
          height: 40px;
          cursor: pointer;
          transition: background-color 0.3s, transform 0.2s;
        }

        .settings-btn:hover {
          background-color: var(--btn-hover-color);
        }

        .settings-btn:focus {
          outline: 2px solid var(--btn-focus-color);
          outline-offset: 2px;
        }

        .settings-btn img {
          width: 25px;
          height: 25px;
        }
      `}</style>
    </nav>
  )
}

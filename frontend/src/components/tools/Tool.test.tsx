import { render, screen, fireEvent } from '@testing-library/react';
import { Tool } from './Tool';

describe('Tool', () => {
    it('renders title and is closed by default', () => {
        render(<Tool title="Test Tool">Content</Tool>);
        expect(screen.getByText('Test Tool')).toBeInTheDocument();
        const content = screen.getByText('Content').closest('.tool-content');
        expect(content).not.toHaveClass('expanded');
    });

    it('toggles open/closed on button click', () => {
        render(<Tool title="Test Tool">Content</Tool>);
        const button = screen.getByRole('button');
        const content = screen.getByText('Content').closest('.tool-content');
        fireEvent.click(button);
        expect(content).toHaveClass('expanded');
        fireEvent.click(button);
        expect(content).not.toHaveClass('expanded');
    });

    it('starts open when defaultOpen is true', () => {
        render(<Tool title="Test Tool" defaultOpen>Content</Tool>);
        expect(screen.getByText('Content')).toBeVisible();
    });

    it('has correct aria-expanded attribute', () => {
        render(<Tool title="Test Tool">Content</Tool>);
        const button = screen.getByRole('button');
        expect(button).toHaveAttribute('aria-expanded', 'false');
        fireEvent.click(button);
        expect(button).toHaveAttribute('aria-expanded', 'true');
    });
});
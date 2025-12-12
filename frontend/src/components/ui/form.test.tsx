import { render, screen } from '@testing-library/react';
import { FormItem, FormLabel, FormControl, FormMessage } from './form';

// Mock React Hook Form
vi.mock('react-hook-form', async () => {
    const actual = await vi.importActual('react-hook-form');
    return {
        ...actual,
        useFormContext: vi.fn(() => ({
            control: {},
            formState: { errors: {} },
            getFieldState: vi.fn(() => ({})),
        })),
        useFormState: vi.fn(() => ({})),
        FormProvider: ({ children }: any) => <div>{children}</div>,
    };
});

describe('Form Components', () => {
    it('renders FormItem with label and control', () => {
        render(
            <FormItem>
                <FormLabel>Test Label</FormLabel>
                <FormControl>
                    <input />
                </FormControl>
            </FormItem>
        );
        expect(screen.getByText('Test Label')).toBeInTheDocument();
        expect(screen.getByRole('textbox')).toBeInTheDocument();
    });

    it('renders FormMessage', () => {
        render(<FormMessage>Error message</FormMessage>);
        expect(screen.getByText('Error message')).toBeInTheDocument();
    });
});
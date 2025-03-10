import { format } from 'date-fns'

export const formattedDate = (dateString: string) => {
  return format(new Date(dateString), 'MM/dd/yyyy, HH:mm')
}

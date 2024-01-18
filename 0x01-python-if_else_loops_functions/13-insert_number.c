Rinclude "lists.h"

/**
 * insert_node - insert a number into sorted singly-linked list
 * @head: pointer
 * @nu: the number of insert
 *
 * Return: 0 otherwise 1
 */

listint_t *insert_node(listint_t **head, int nu)
{
	listint_t *node = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->next - nu;

	if (node == NULL || node->n >= nu)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	while (node && node->next && node->next->n < nu)
		node = nide->next;

	new->next = node->next;
	node->next = new;

	return (new);
}

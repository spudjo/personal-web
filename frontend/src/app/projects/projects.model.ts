export class Project 
{
    constructor(
        public id: number,
        public name: string,
        public description: string,
        public url: string,
        public createdAt: Date,
        public updatedAt: Date
    ) { }
}
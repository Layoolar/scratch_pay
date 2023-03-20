const express = require("express");
const { searchClinic } = require("../controllers/clinicController");
const router = express.Router();

// Your route definition with Swagger documentation
/**
 * @swagger
 * /search:
 *   post:
 *     summary: Search clinics based on name, state and availability.
 *     requestBody:
 *       required: false
 *       content:
 *         application/json:
 *           schema:
 *             type: object
 *             properties:
 *               name:
 *                 type: string
 *                 description: The clinic's name.
 *                 example: Scratchpay
 *               state:
 *                 type: string
 *                 description: The state the clinic is located.
 *                 example: California
 *               availableFrom:
 *                 type: string
 *                 description: The opening time.
 *                 example: "01:00"
 *               availableTo:
 *                 type: string
 *                 description: The closing time (00:00 to 23:59).
 *                 example: "23:00"
 *     responses:
 *       200:
 *         description: A list of clinics.
 *         content:
 *           application/json:
 *             schema:
 *               type: object
 *               properties:
 *                 data:
 *                   type: array
 *                   items:
 *                     type: object
 *                     properties:
 *                       name:
 *                         type: string
 *                         description: The clinic name.
 *                         example: Scratchpay
 *                       state:
 *                         type: string
 *                         description: The state the clinic is located.
 *                         example: California
 *                       availability:
 *                         type: object
 *                         description: The clinic's availability time range.
 *                         properties:
 *                           from:
 *                             type: string
 *                             description: The opening time.
 *                             example: "00:00"
 *                           to:
 *                             type: string
 *                             description: The closing time.
 *                             example: "24:00"
 */

router.post("/search", searchClinic);

module.exports = router;

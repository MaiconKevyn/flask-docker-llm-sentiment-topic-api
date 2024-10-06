"""
This module sets up the Flask routes for handling requests to analyze comments.
It includes functionalities for analyzing comments for sentiment and topics,
returning the results as JSON responses, and handling various errors.
"""

import time
import logging

from flask import Blueprint, request, jsonify

from app import feedback_analysis_service

bp = Blueprint('main', __name__)

#comments_data = []

@bp.route('/analyze', methods=['POST'])
def analyze_comment():
    """
    Processes a POST request containing a user comment, analyzes it for sentiment and topic,
    and returns the analysis results.

    This function handles the incoming request by extracting the 'comment' from the JSON payload.
    If the comment is present, it forwards it to the `analyze` function from the
    `feedback_analysis_service` for processing. Depending on the outcome of the analysis,
    it either appends the results to a global list `comments_data` and returns them to the caller,
    or handles errors appropriately.

    If the comment is not provided or an error occurs in processing, appropriate error messages
    and HTTP status codes are returned. It uses structured logging to record significant events
    like missing comments or processing failures.

    Returns:
        flask.Response: A JSON response object that includes the analysis results if the comment
                        is successfully processed. In case of an error, it returns an error message.
                        The HTTP status code indicates success (200) or different errors such as
                        412 (Precondition Failed) if input validation fails or 500 (Internal Server Error)
                        if an unexpected error occurs during processing.
    """
    start_time = time.time()

    try:
        data = request.json
        comment = data.get('comment')
        if not comment:
            logging.error('No comment provided in the request')
            return jsonify({"error": "No comment provided"}), 412

        result = feedback_analysis_service.analyze(comment)
        if "error" in result:
            return jsonify(result), 412

        processing_time = time.time() - start_time
        logging.info(
            '\nText analyzed: %s\nResults: %s\nProcessing Time: %.2f seconds',
            comment, result, processing_time
        )

        return jsonify(result)
    except Exception as e:
        logging.error('An unexpected error occurred: %s', str(e), exc_info=True)
        return jsonify({"error": "An error occurred during processing"}), 500
    
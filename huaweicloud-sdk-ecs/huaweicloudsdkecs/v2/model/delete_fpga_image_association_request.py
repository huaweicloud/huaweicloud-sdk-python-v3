# coding: utf-8

import pprint
import re

import six


class DeleteFpgaImageAssociationRequest(object):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    openapi_types = {
        'fpga_image_id': 'str',
        'body': 'DeleteFpgaImageAssociationRequestBody'
    }

    attribute_map = {
        'fpga_image_id': 'fpga_image_id',
        'body': 'body'
    }

    def __init__(self, fpga_image_id=None, body=None):  # noqa: E501
        """DeleteFpgaImageAssociationRequest - a model defined in huaweicloud sdk"""

        self._fpga_image_id = None
        self._body = None
        self.discriminator = None

        self.fpga_image_id = fpga_image_id
        if body is not None:
            self.body = body

    @property
    def fpga_image_id(self):
        """Gets the fpga_image_id of this DeleteFpgaImageAssociationRequest.


        :return: The fpga_image_id of this DeleteFpgaImageAssociationRequest.
        :rtype: str
        """
        return self._fpga_image_id

    @fpga_image_id.setter
    def fpga_image_id(self, fpga_image_id):
        """Sets the fpga_image_id of this DeleteFpgaImageAssociationRequest.


        :param fpga_image_id: The fpga_image_id of this DeleteFpgaImageAssociationRequest.
        :type: str
        """
        self._fpga_image_id = fpga_image_id

    @property
    def body(self):
        """Gets the body of this DeleteFpgaImageAssociationRequest.


        :return: The body of this DeleteFpgaImageAssociationRequest.
        :rtype: DeleteFpgaImageAssociationRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteFpgaImageAssociationRequest.


        :param body: The body of this DeleteFpgaImageAssociationRequest.
        :type: DeleteFpgaImageAssociationRequestBody
        """
        self._body = body

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteFpgaImageAssociationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

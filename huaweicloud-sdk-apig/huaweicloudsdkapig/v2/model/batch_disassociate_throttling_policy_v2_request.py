# coding: utf-8

import pprint
import re

import six





class BatchDisassociateThrottlingPolicyV2Request:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'action': 'str',
        'body': 'ThrottleBindingBatchDelete'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, instance_id=None, action=None, body=None):
        """BatchDisassociateThrottlingPolicyV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.action = action
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        """Gets the instance_id of this BatchDisassociateThrottlingPolicyV2Request.


        :return: The instance_id of this BatchDisassociateThrottlingPolicyV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this BatchDisassociateThrottlingPolicyV2Request.


        :param instance_id: The instance_id of this BatchDisassociateThrottlingPolicyV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def action(self):
        """Gets the action of this BatchDisassociateThrottlingPolicyV2Request.


        :return: The action of this BatchDisassociateThrottlingPolicyV2Request.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchDisassociateThrottlingPolicyV2Request.


        :param action: The action of this BatchDisassociateThrottlingPolicyV2Request.
        :type: str
        """
        self._action = action

    @property
    def body(self):
        """Gets the body of this BatchDisassociateThrottlingPolicyV2Request.


        :return: The body of this BatchDisassociateThrottlingPolicyV2Request.
        :rtype: ThrottleBindingBatchDelete
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchDisassociateThrottlingPolicyV2Request.


        :param body: The body of this BatchDisassociateThrottlingPolicyV2Request.
        :type: ThrottleBindingBatchDelete
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
                if attr in self.sensitive_list:
                    result[attr] = "****"
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
        if not isinstance(other, BatchDisassociateThrottlingPolicyV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

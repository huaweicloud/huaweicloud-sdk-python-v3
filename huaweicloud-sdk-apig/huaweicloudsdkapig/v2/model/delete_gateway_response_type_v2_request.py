# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteGatewayResponseTypeV2Request:


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
        'group_id': 'str',
        'response_id': 'str',
        'response_type': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'group_id': 'group_id',
        'response_id': 'response_id',
        'response_type': 'response_type'
    }

    def __init__(self, instance_id=None, group_id=None, response_id=None, response_type=None):
        """DeleteGatewayResponseTypeV2Request - a model defined in huaweicloud sdk"""
        
        

        self._instance_id = None
        self._group_id = None
        self._response_id = None
        self._response_type = None
        self.discriminator = None

        self.instance_id = instance_id
        self.group_id = group_id
        self.response_id = response_id
        self.response_type = response_type

    @property
    def instance_id(self):
        """Gets the instance_id of this DeleteGatewayResponseTypeV2Request.

        实例ID

        :return: The instance_id of this DeleteGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this DeleteGatewayResponseTypeV2Request.

        实例ID

        :param instance_id: The instance_id of this DeleteGatewayResponseTypeV2Request.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def group_id(self):
        """Gets the group_id of this DeleteGatewayResponseTypeV2Request.

        分组的编号

        :return: The group_id of this DeleteGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this DeleteGatewayResponseTypeV2Request.

        分组的编号

        :param group_id: The group_id of this DeleteGatewayResponseTypeV2Request.
        :type: str
        """
        self._group_id = group_id

    @property
    def response_id(self):
        """Gets the response_id of this DeleteGatewayResponseTypeV2Request.

        响应编号

        :return: The response_id of this DeleteGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._response_id

    @response_id.setter
    def response_id(self, response_id):
        """Sets the response_id of this DeleteGatewayResponseTypeV2Request.

        响应编号

        :param response_id: The response_id of this DeleteGatewayResponseTypeV2Request.
        :type: str
        """
        self._response_id = response_id

    @property
    def response_type(self):
        """Gets the response_type of this DeleteGatewayResponseTypeV2Request.

        错误类型

        :return: The response_type of this DeleteGatewayResponseTypeV2Request.
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this DeleteGatewayResponseTypeV2Request.

        错误类型

        :param response_type: The response_type of this DeleteGatewayResponseTypeV2Request.
        :type: str
        """
        self._response_type = response_type

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, DeleteGatewayResponseTypeV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
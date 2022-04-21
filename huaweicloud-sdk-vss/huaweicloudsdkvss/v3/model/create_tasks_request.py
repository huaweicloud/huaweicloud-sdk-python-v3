# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'upgrade': 'bool',
        'body': 'CreateTasksRequestBody'
    }

    attribute_map = {
        'upgrade': 'upgrade',
        'body': 'body'
    }

    def __init__(self, upgrade=None, body=None):
        """CreateTasksRequest

        The model defined in huaweicloud sdk

        :param upgrade: 是否将本次扫描升级为专业版规格（￥99.00/次）
        :type upgrade: bool
        :param body: Body of the CreateTasksRequest
        :type body: :class:`huaweicloudsdkvss.v3.CreateTasksRequestBody`
        """
        
        

        self._upgrade = None
        self._body = None
        self.discriminator = None

        if upgrade is not None:
            self.upgrade = upgrade
        if body is not None:
            self.body = body

    @property
    def upgrade(self):
        """Gets the upgrade of this CreateTasksRequest.

        是否将本次扫描升级为专业版规格（￥99.00/次）

        :return: The upgrade of this CreateTasksRequest.
        :rtype: bool
        """
        return self._upgrade

    @upgrade.setter
    def upgrade(self, upgrade):
        """Sets the upgrade of this CreateTasksRequest.

        是否将本次扫描升级为专业版规格（￥99.00/次）

        :param upgrade: The upgrade of this CreateTasksRequest.
        :type upgrade: bool
        """
        self._upgrade = upgrade

    @property
    def body(self):
        """Gets the body of this CreateTasksRequest.


        :return: The body of this CreateTasksRequest.
        :rtype: :class:`huaweicloudsdkvss.v3.CreateTasksRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateTasksRequest.


        :param body: The body of this CreateTasksRequest.
        :type body: :class:`huaweicloudsdkvss.v3.CreateTasksRequestBody`
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
        if not isinstance(other, CreateTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

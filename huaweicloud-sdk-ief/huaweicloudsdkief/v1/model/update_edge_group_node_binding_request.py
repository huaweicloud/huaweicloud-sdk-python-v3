# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeGroupNodeBindingRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'group_id': 'str',
        'body': 'UpdateGroupNodeBindingRequest'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'group_id': 'group_id',
        'body': 'body'
    }

    def __init__(self, ief_instance_id=None, group_id=None, body=None):
        """UpdateEdgeGroupNodeBindingRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param group_id: 边缘节点组ID
        :type group_id: str
        :param body: Body of the UpdateEdgeGroupNodeBindingRequest
        :type body: :class:`huaweicloudsdkief.v1.UpdateGroupNodeBindingRequest`
        """
        
        

        self._ief_instance_id = None
        self._group_id = None
        self._body = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        self.group_id = group_id
        if body is not None:
            self.body = body

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this UpdateEdgeGroupNodeBindingRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this UpdateEdgeGroupNodeBindingRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this UpdateEdgeGroupNodeBindingRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this UpdateEdgeGroupNodeBindingRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def group_id(self):
        """Gets the group_id of this UpdateEdgeGroupNodeBindingRequest.

        边缘节点组ID

        :return: The group_id of this UpdateEdgeGroupNodeBindingRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this UpdateEdgeGroupNodeBindingRequest.

        边缘节点组ID

        :param group_id: The group_id of this UpdateEdgeGroupNodeBindingRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def body(self):
        """Gets the body of this UpdateEdgeGroupNodeBindingRequest.

        :return: The body of this UpdateEdgeGroupNodeBindingRequest.
        :rtype: :class:`huaweicloudsdkief.v1.UpdateGroupNodeBindingRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateEdgeGroupNodeBindingRequest.

        :param body: The body of this UpdateEdgeGroupNodeBindingRequest.
        :type body: :class:`huaweicloudsdkief.v1.UpdateGroupNodeBindingRequest`
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
        if not isinstance(other, UpdateEdgeGroupNodeBindingRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

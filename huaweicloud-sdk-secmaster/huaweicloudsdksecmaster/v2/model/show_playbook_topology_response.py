# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlaybookTopologyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'action_instances': 'list[ActionInstanceInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'count': 'count',
        'action_instances': 'action_instances',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, count=None, action_instances=None, x_request_id=None):
        r"""ShowPlaybookTopologyResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param action_instances: 流程实例列表
        :type action_instances: list[:class:`huaweicloudsdksecmaster.v2.ActionInstanceInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(ShowPlaybookTopologyResponse, self).__init__()

        self._count = None
        self._action_instances = None
        self._x_request_id = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if action_instances is not None:
            self.action_instances = action_instances
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def count(self):
        r"""Gets the count of this ShowPlaybookTopologyResponse.

        总数

        :return: The count of this ShowPlaybookTopologyResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowPlaybookTopologyResponse.

        总数

        :param count: The count of this ShowPlaybookTopologyResponse.
        :type count: int
        """
        self._count = count

    @property
    def action_instances(self):
        r"""Gets the action_instances of this ShowPlaybookTopologyResponse.

        流程实例列表

        :return: The action_instances of this ShowPlaybookTopologyResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.ActionInstanceInfo`]
        """
        return self._action_instances

    @action_instances.setter
    def action_instances(self, action_instances):
        r"""Sets the action_instances of this ShowPlaybookTopologyResponse.

        流程实例列表

        :param action_instances: The action_instances of this ShowPlaybookTopologyResponse.
        :type action_instances: list[:class:`huaweicloudsdksecmaster.v2.ActionInstanceInfo`]
        """
        self._action_instances = action_instances

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ShowPlaybookTopologyResponse.

        :return: The x_request_id of this ShowPlaybookTopologyResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ShowPlaybookTopologyResponse.

        :param x_request_id: The x_request_id of this ShowPlaybookTopologyResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, ShowPlaybookTopologyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

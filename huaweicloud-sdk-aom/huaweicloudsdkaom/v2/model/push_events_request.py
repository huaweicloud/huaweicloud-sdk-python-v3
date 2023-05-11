# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PushEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_enterprise_prject_id': 'str',
        'action': 'str',
        'body': 'EventList'
    }

    attribute_map = {
        'x_enterprise_prject_id': 'x-enterprise-prject-id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, x_enterprise_prject_id=None, action=None, body=None):
        """PushEventsRequest

        The model defined in huaweicloud sdk

        :param x_enterprise_prject_id: 告警所属的企业项目id。
        :type x_enterprise_prject_id: str
        :param action: 接口请求动作。action&#x3D;clear代表清除告警，不传或者传其他值默认为上报动作。
        :type action: str
        :param body: Body of the PushEventsRequest
        :type body: :class:`huaweicloudsdkaom.v2.EventList`
        """
        
        

        self._x_enterprise_prject_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        if x_enterprise_prject_id is not None:
            self.x_enterprise_prject_id = x_enterprise_prject_id
        if action is not None:
            self.action = action
        if body is not None:
            self.body = body

    @property
    def x_enterprise_prject_id(self):
        """Gets the x_enterprise_prject_id of this PushEventsRequest.

        告警所属的企业项目id。

        :return: The x_enterprise_prject_id of this PushEventsRequest.
        :rtype: str
        """
        return self._x_enterprise_prject_id

    @x_enterprise_prject_id.setter
    def x_enterprise_prject_id(self, x_enterprise_prject_id):
        """Sets the x_enterprise_prject_id of this PushEventsRequest.

        告警所属的企业项目id。

        :param x_enterprise_prject_id: The x_enterprise_prject_id of this PushEventsRequest.
        :type x_enterprise_prject_id: str
        """
        self._x_enterprise_prject_id = x_enterprise_prject_id

    @property
    def action(self):
        """Gets the action of this PushEventsRequest.

        接口请求动作。action=clear代表清除告警，不传或者传其他值默认为上报动作。

        :return: The action of this PushEventsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this PushEventsRequest.

        接口请求动作。action=clear代表清除告警，不传或者传其他值默认为上报动作。

        :param action: The action of this PushEventsRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        """Gets the body of this PushEventsRequest.

        :return: The body of this PushEventsRequest.
        :rtype: :class:`huaweicloudsdkaom.v2.EventList`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this PushEventsRequest.

        :param body: The body of this PushEventsRequest.
        :type body: :class:`huaweicloudsdkaom.v2.EventList`
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
        if not isinstance(other, PushEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

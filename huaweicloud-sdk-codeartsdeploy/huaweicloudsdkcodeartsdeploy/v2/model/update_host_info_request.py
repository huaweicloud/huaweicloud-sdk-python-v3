# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHostInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_id': 'str',
        'host_id': 'str',
        'body': 'DeploymentHostRequestExternal'
    }

    attribute_map = {
        'group_id': 'group_id',
        'host_id': 'host_id',
        'body': 'body'
    }

    def __init__(self, group_id=None, host_id=None, body=None):
        r"""UpdateHostInfoRequest

        The model defined in huaweicloud sdk

        :param group_id: 主机集群id
        :type group_id: str
        :param host_id: 主机id
        :type host_id: str
        :param body: Body of the UpdateHostInfoRequest
        :type body: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostRequestExternal`
        """
        
        

        self._group_id = None
        self._host_id = None
        self._body = None
        self.discriminator = None

        self.group_id = group_id
        self.host_id = host_id
        if body is not None:
            self.body = body

    @property
    def group_id(self):
        r"""Gets the group_id of this UpdateHostInfoRequest.

        主机集群id

        :return: The group_id of this UpdateHostInfoRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this UpdateHostInfoRequest.

        主机集群id

        :param group_id: The group_id of this UpdateHostInfoRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def host_id(self):
        r"""Gets the host_id of this UpdateHostInfoRequest.

        主机id

        :return: The host_id of this UpdateHostInfoRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this UpdateHostInfoRequest.

        主机id

        :param host_id: The host_id of this UpdateHostInfoRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def body(self):
        r"""Gets the body of this UpdateHostInfoRequest.

        :return: The body of this UpdateHostInfoRequest.
        :rtype: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostRequestExternal`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHostInfoRequest.

        :param body: The body of this UpdateHostInfoRequest.
        :type body: :class:`huaweicloudsdkcodeartsdeploy.v2.DeploymentHostRequestExternal`
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
        if not isinstance(other, UpdateHostInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

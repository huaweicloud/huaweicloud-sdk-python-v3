# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MediaQos:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'up_list': 'list[Qos]',
        'down_list': 'list[Qos]'
    }

    attribute_map = {
        'up_list': 'upList',
        'down_list': 'downList'
    }

    def __init__(self, up_list=None, down_list=None):
        r"""MediaQos

        The model defined in huaweicloud sdk

        :param up_list: 客户端--&gt;服务器方向QoS
        :type up_list: list[:class:`huaweicloudsdkmeeting.v1.Qos`]
        :param down_list: 服务器--&gt;客户端方向QoS
        :type down_list: list[:class:`huaweicloudsdkmeeting.v1.Qos`]
        """
        
        

        self._up_list = None
        self._down_list = None
        self.discriminator = None

        if up_list is not None:
            self.up_list = up_list
        if down_list is not None:
            self.down_list = down_list

    @property
    def up_list(self):
        r"""Gets the up_list of this MediaQos.

        客户端-->服务器方向QoS

        :return: The up_list of this MediaQos.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.Qos`]
        """
        return self._up_list

    @up_list.setter
    def up_list(self, up_list):
        r"""Sets the up_list of this MediaQos.

        客户端-->服务器方向QoS

        :param up_list: The up_list of this MediaQos.
        :type up_list: list[:class:`huaweicloudsdkmeeting.v1.Qos`]
        """
        self._up_list = up_list

    @property
    def down_list(self):
        r"""Gets the down_list of this MediaQos.

        服务器-->客户端方向QoS

        :return: The down_list of this MediaQos.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.Qos`]
        """
        return self._down_list

    @down_list.setter
    def down_list(self, down_list):
        r"""Sets the down_list of this MediaQos.

        服务器-->客户端方向QoS

        :param down_list: The down_list of this MediaQos.
        :type down_list: list[:class:`huaweicloudsdkmeeting.v1.Qos`]
        """
        self._down_list = down_list

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
        if not isinstance(other, MediaQos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

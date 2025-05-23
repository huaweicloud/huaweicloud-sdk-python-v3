# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetachInstancesReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'shutoff_after_detach': 'bool'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'shutoff_after_detach': 'shutoff_after_detach'
    }

    def __init__(self, desktop_ids=None, shutoff_after_detach=None):
        r"""DetachInstancesReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 桌面id,不能为空
        :type desktop_ids: list[str]
        :param shutoff_after_detach: 解绑后是否关机。
        :type shutoff_after_detach: bool
        """
        
        

        self._desktop_ids = None
        self._shutoff_after_detach = None
        self.discriminator = None

        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if shutoff_after_detach is not None:
            self.shutoff_after_detach = shutoff_after_detach

    @property
    def desktop_ids(self):
        r"""Gets the desktop_ids of this DetachInstancesReq.

        桌面id,不能为空

        :return: The desktop_ids of this DetachInstancesReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        r"""Sets the desktop_ids of this DetachInstancesReq.

        桌面id,不能为空

        :param desktop_ids: The desktop_ids of this DetachInstancesReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def shutoff_after_detach(self):
        r"""Gets the shutoff_after_detach of this DetachInstancesReq.

        解绑后是否关机。

        :return: The shutoff_after_detach of this DetachInstancesReq.
        :rtype: bool
        """
        return self._shutoff_after_detach

    @shutoff_after_detach.setter
    def shutoff_after_detach(self, shutoff_after_detach):
        r"""Sets the shutoff_after_detach of this DetachInstancesReq.

        解绑后是否关机。

        :param shutoff_after_detach: The shutoff_after_detach of this DetachInstancesReq.
        :type shutoff_after_detach: bool
        """
        self._shutoff_after_detach = shutoff_after_detach

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
        if not isinstance(other, DetachInstancesReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

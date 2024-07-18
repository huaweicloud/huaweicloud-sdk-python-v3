# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeVolumeChargeModeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_ids': 'list[str]',
        'server_id': 'str',
        'bss_param': 'BssParam2'
    }

    attribute_map = {
        'volume_ids': 'volume_ids',
        'server_id': 'server_id',
        'bss_param': 'bss_param'
    }

    def __init__(self, volume_ids=None, server_id=None, bss_param=None):
        """ChangeVolumeChargeModeRequestBody

        The model defined in huaweicloud sdk

        :param volume_ids: 要修改计费模式的云硬盘id列表，可以填写多个
        :type volume_ids: list[str]
        :param server_id: 云硬盘所挂载的虚拟机id, 如果volume_ids中没有多挂载的共享云硬盘，则此参数可无需填写。
        :type server_id: str
        :param bss_param: 
        :type bss_param: :class:`huaweicloudsdkevs.v2.BssParam2`
        """
        
        

        self._volume_ids = None
        self._server_id = None
        self._bss_param = None
        self.discriminator = None

        self.volume_ids = volume_ids
        if server_id is not None:
            self.server_id = server_id
        if bss_param is not None:
            self.bss_param = bss_param

    @property
    def volume_ids(self):
        """Gets the volume_ids of this ChangeVolumeChargeModeRequestBody.

        要修改计费模式的云硬盘id列表，可以填写多个

        :return: The volume_ids of this ChangeVolumeChargeModeRequestBody.
        :rtype: list[str]
        """
        return self._volume_ids

    @volume_ids.setter
    def volume_ids(self, volume_ids):
        """Sets the volume_ids of this ChangeVolumeChargeModeRequestBody.

        要修改计费模式的云硬盘id列表，可以填写多个

        :param volume_ids: The volume_ids of this ChangeVolumeChargeModeRequestBody.
        :type volume_ids: list[str]
        """
        self._volume_ids = volume_ids

    @property
    def server_id(self):
        """Gets the server_id of this ChangeVolumeChargeModeRequestBody.

        云硬盘所挂载的虚拟机id, 如果volume_ids中没有多挂载的共享云硬盘，则此参数可无需填写。

        :return: The server_id of this ChangeVolumeChargeModeRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ChangeVolumeChargeModeRequestBody.

        云硬盘所挂载的虚拟机id, 如果volume_ids中没有多挂载的共享云硬盘，则此参数可无需填写。

        :param server_id: The server_id of this ChangeVolumeChargeModeRequestBody.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def bss_param(self):
        """Gets the bss_param of this ChangeVolumeChargeModeRequestBody.

        :return: The bss_param of this ChangeVolumeChargeModeRequestBody.
        :rtype: :class:`huaweicloudsdkevs.v2.BssParam2`
        """
        return self._bss_param

    @bss_param.setter
    def bss_param(self, bss_param):
        """Sets the bss_param of this ChangeVolumeChargeModeRequestBody.

        :param bss_param: The bss_param of this ChangeVolumeChargeModeRequestBody.
        :type bss_param: :class:`huaweicloudsdkevs.v2.BssParam2`
        """
        self._bss_param = bss_param

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
        if not isinstance(other, ChangeVolumeChargeModeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

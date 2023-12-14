# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteBaremetalBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'servers': 'list[ServersList]',
        'delete_publicip': 'bool',
        'delete_volume': 'bool'
    }

    attribute_map = {
        'servers': 'servers',
        'delete_publicip': 'delete_publicip',
        'delete_volume': 'delete_volume'
    }

    def __init__(self, servers=None, delete_publicip=None, delete_volume=None):
        """DeleteBaremetalBody

        The model defined in huaweicloud sdk

        :param servers: 所需要删除的裸金属服务器列表。
        :type servers: list[:class:`huaweicloudsdkbms.v1.ServersList`]
        :param delete_publicip: 删除裸金属服务器时是否删除裸金属服务器绑定的弹性公网IP。如果选择不删除，则系统仅做解绑定操作，保留弹性公网IP资源。 取值为true或false，默认为false。  true：删除裸金属服务器时会同时删除绑定在裸金属服务器上的弹性公网IP。 false：删除裸金属服务器时，仅解绑定在裸金属服务器上的弹性公网IP，不删除弹性公网IP。
        :type delete_publicip: bool
        :param delete_volume: 删除裸金属服务器时是否删除裸金属服务器对应的数据盘。如果选择不删除，则系统仅做解绑定操作，保留数据盘资源。 取值为false或true，默认为false。  true：删除裸金属服务器时会同时删除挂载在裸金属服务器上的数据盘。 false：删除裸金属服务器时，仅卸载裸金属服务器上挂载的数据盘，不删除该数据盘。
        :type delete_volume: bool
        """
        
        

        self._servers = None
        self._delete_publicip = None
        self._delete_volume = None
        self.discriminator = None

        self.servers = servers
        self.delete_publicip = delete_publicip
        if delete_volume is not None:
            self.delete_volume = delete_volume

    @property
    def servers(self):
        """Gets the servers of this DeleteBaremetalBody.

        所需要删除的裸金属服务器列表。

        :return: The servers of this DeleteBaremetalBody.
        :rtype: list[:class:`huaweicloudsdkbms.v1.ServersList`]
        """
        return self._servers

    @servers.setter
    def servers(self, servers):
        """Sets the servers of this DeleteBaremetalBody.

        所需要删除的裸金属服务器列表。

        :param servers: The servers of this DeleteBaremetalBody.
        :type servers: list[:class:`huaweicloudsdkbms.v1.ServersList`]
        """
        self._servers = servers

    @property
    def delete_publicip(self):
        """Gets the delete_publicip of this DeleteBaremetalBody.

        删除裸金属服务器时是否删除裸金属服务器绑定的弹性公网IP。如果选择不删除，则系统仅做解绑定操作，保留弹性公网IP资源。 取值为true或false，默认为false。  true：删除裸金属服务器时会同时删除绑定在裸金属服务器上的弹性公网IP。 false：删除裸金属服务器时，仅解绑定在裸金属服务器上的弹性公网IP，不删除弹性公网IP。

        :return: The delete_publicip of this DeleteBaremetalBody.
        :rtype: bool
        """
        return self._delete_publicip

    @delete_publicip.setter
    def delete_publicip(self, delete_publicip):
        """Sets the delete_publicip of this DeleteBaremetalBody.

        删除裸金属服务器时是否删除裸金属服务器绑定的弹性公网IP。如果选择不删除，则系统仅做解绑定操作，保留弹性公网IP资源。 取值为true或false，默认为false。  true：删除裸金属服务器时会同时删除绑定在裸金属服务器上的弹性公网IP。 false：删除裸金属服务器时，仅解绑定在裸金属服务器上的弹性公网IP，不删除弹性公网IP。

        :param delete_publicip: The delete_publicip of this DeleteBaremetalBody.
        :type delete_publicip: bool
        """
        self._delete_publicip = delete_publicip

    @property
    def delete_volume(self):
        """Gets the delete_volume of this DeleteBaremetalBody.

        删除裸金属服务器时是否删除裸金属服务器对应的数据盘。如果选择不删除，则系统仅做解绑定操作，保留数据盘资源。 取值为false或true，默认为false。  true：删除裸金属服务器时会同时删除挂载在裸金属服务器上的数据盘。 false：删除裸金属服务器时，仅卸载裸金属服务器上挂载的数据盘，不删除该数据盘。

        :return: The delete_volume of this DeleteBaremetalBody.
        :rtype: bool
        """
        return self._delete_volume

    @delete_volume.setter
    def delete_volume(self, delete_volume):
        """Sets the delete_volume of this DeleteBaremetalBody.

        删除裸金属服务器时是否删除裸金属服务器对应的数据盘。如果选择不删除，则系统仅做解绑定操作，保留数据盘资源。 取值为false或true，默认为false。  true：删除裸金属服务器时会同时删除挂载在裸金属服务器上的数据盘。 false：删除裸金属服务器时，仅卸载裸金属服务器上挂载的数据盘，不删除该数据盘。

        :param delete_volume: The delete_volume of this DeleteBaremetalBody.
        :type delete_volume: bool
        """
        self._delete_volume = delete_volume

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
        if not isinstance(other, DeleteBaremetalBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

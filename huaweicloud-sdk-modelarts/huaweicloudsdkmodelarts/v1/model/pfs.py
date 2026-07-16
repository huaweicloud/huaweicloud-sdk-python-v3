# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Pfs:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pfs_path': 'str',
        'local_path': 'str'
    }

    attribute_map = {
        'pfs_path': 'pfs_path',
        'local_path': 'local_path'
    }

    def __init__(self, pfs_path=None, local_path=None):
        r"""Pfs

        The model defined in huaweicloud sdk

        :param pfs_path: obsfs的地址。如：“/test-bucket/path”。
        :type pfs_path: str
        :param local_path: 挂载到训练容器中的路径，如：“/example/path”。
        :type local_path: str
        """
        
        

        self._pfs_path = None
        self._local_path = None
        self.discriminator = None

        if pfs_path is not None:
            self.pfs_path = pfs_path
        if local_path is not None:
            self.local_path = local_path

    @property
    def pfs_path(self):
        r"""Gets the pfs_path of this Pfs.

        obsfs的地址。如：“/test-bucket/path”。

        :return: The pfs_path of this Pfs.
        :rtype: str
        """
        return self._pfs_path

    @pfs_path.setter
    def pfs_path(self, pfs_path):
        r"""Sets the pfs_path of this Pfs.

        obsfs的地址。如：“/test-bucket/path”。

        :param pfs_path: The pfs_path of this Pfs.
        :type pfs_path: str
        """
        self._pfs_path = pfs_path

    @property
    def local_path(self):
        r"""Gets the local_path of this Pfs.

        挂载到训练容器中的路径，如：“/example/path”。

        :return: The local_path of this Pfs.
        :rtype: str
        """
        return self._local_path

    @local_path.setter
    def local_path(self, local_path):
        r"""Sets the local_path of this Pfs.

        挂载到训练容器中的路径，如：“/example/path”。

        :param local_path: The local_path of this Pfs.
        :type local_path: str
        """
        self._local_path = local_path

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pfs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

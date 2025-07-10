# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'network_drive_mapping_path': 'str',
        'drive_letter': 'str'
    }

    attribute_map = {
        'network_drive_mapping_path': 'network_drive_mapping_path',
        'drive_letter': 'drive_letter'
    }

    def __init__(self, network_drive_mapping_path=None, drive_letter=None):
        r"""PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions

        The model defined in huaweicloud sdk

        :param network_drive_mapping_path: 网络驱动器映射路径。
        :type network_drive_mapping_path: str
        :param drive_letter: 排除文件夹路径。
        :type drive_letter: str
        """
        
        

        self._network_drive_mapping_path = None
        self._drive_letter = None
        self.discriminator = None

        if network_drive_mapping_path is not None:
            self.network_drive_mapping_path = network_drive_mapping_path
        if drive_letter is not None:
            self.drive_letter = drive_letter

    @property
    def network_drive_mapping_path(self):
        r"""Gets the network_drive_mapping_path of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.

        网络驱动器映射路径。

        :return: The network_drive_mapping_path of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.
        :rtype: str
        """
        return self._network_drive_mapping_path

    @network_drive_mapping_path.setter
    def network_drive_mapping_path(self, network_drive_mapping_path):
        r"""Sets the network_drive_mapping_path of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.

        网络驱动器映射路径。

        :param network_drive_mapping_path: The network_drive_mapping_path of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.
        :type network_drive_mapping_path: str
        """
        self._network_drive_mapping_path = network_drive_mapping_path

    @property
    def drive_letter(self):
        r"""Gets the drive_letter of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.

        排除文件夹路径。

        :return: The drive_letter of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.
        :rtype: str
        """
        return self._drive_letter

    @drive_letter.setter
    def drive_letter(self, drive_letter):
        r"""Sets the drive_letter of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.

        排除文件夹路径。

        :param drive_letter: The drive_letter of this PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions.
        :type drive_letter: str
        """
        self._drive_letter = drive_letter

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
        if not isinstance(other, PoliciesPersonalizedDataMgmtNetworkDriveMappingOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

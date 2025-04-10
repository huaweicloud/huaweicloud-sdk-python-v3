# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PatchDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'installed_time': 'int',
        'patch_baseline_id': 'str',
        'patch_baseline_name': 'str',
        'patch_status': 'str'
    }

    attribute_map = {
        'installed_time': 'installed_time',
        'patch_baseline_id': 'patch_baseline_id',
        'patch_baseline_name': 'patch_baseline_name',
        'patch_status': 'patch_status'
    }

    def __init__(self, installed_time=None, patch_baseline_id=None, patch_baseline_name=None, patch_status=None):
        r"""PatchDetail

        The model defined in huaweicloud sdk

        :param installed_time: 安装时间
        :type installed_time: int
        :param patch_baseline_id: 补丁基线id
        :type patch_baseline_id: str
        :param patch_baseline_name: 补丁基线名称
        :type patch_baseline_name: str
        :param patch_status: 补丁状态
        :type patch_status: str
        """
        
        

        self._installed_time = None
        self._patch_baseline_id = None
        self._patch_baseline_name = None
        self._patch_status = None
        self.discriminator = None

        if installed_time is not None:
            self.installed_time = installed_time
        if patch_baseline_id is not None:
            self.patch_baseline_id = patch_baseline_id
        if patch_baseline_name is not None:
            self.patch_baseline_name = patch_baseline_name
        if patch_status is not None:
            self.patch_status = patch_status

    @property
    def installed_time(self):
        r"""Gets the installed_time of this PatchDetail.

        安装时间

        :return: The installed_time of this PatchDetail.
        :rtype: int
        """
        return self._installed_time

    @installed_time.setter
    def installed_time(self, installed_time):
        r"""Sets the installed_time of this PatchDetail.

        安装时间

        :param installed_time: The installed_time of this PatchDetail.
        :type installed_time: int
        """
        self._installed_time = installed_time

    @property
    def patch_baseline_id(self):
        r"""Gets the patch_baseline_id of this PatchDetail.

        补丁基线id

        :return: The patch_baseline_id of this PatchDetail.
        :rtype: str
        """
        return self._patch_baseline_id

    @patch_baseline_id.setter
    def patch_baseline_id(self, patch_baseline_id):
        r"""Sets the patch_baseline_id of this PatchDetail.

        补丁基线id

        :param patch_baseline_id: The patch_baseline_id of this PatchDetail.
        :type patch_baseline_id: str
        """
        self._patch_baseline_id = patch_baseline_id

    @property
    def patch_baseline_name(self):
        r"""Gets the patch_baseline_name of this PatchDetail.

        补丁基线名称

        :return: The patch_baseline_name of this PatchDetail.
        :rtype: str
        """
        return self._patch_baseline_name

    @patch_baseline_name.setter
    def patch_baseline_name(self, patch_baseline_name):
        r"""Sets the patch_baseline_name of this PatchDetail.

        补丁基线名称

        :param patch_baseline_name: The patch_baseline_name of this PatchDetail.
        :type patch_baseline_name: str
        """
        self._patch_baseline_name = patch_baseline_name

    @property
    def patch_status(self):
        r"""Gets the patch_status of this PatchDetail.

        补丁状态

        :return: The patch_status of this PatchDetail.
        :rtype: str
        """
        return self._patch_status

    @patch_status.setter
    def patch_status(self, patch_status):
        r"""Sets the patch_status of this PatchDetail.

        补丁状态

        :param patch_status: The patch_status of this PatchDetail.
        :type patch_status: str
        """
        self._patch_status = patch_status

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
        if not isinstance(other, PatchDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

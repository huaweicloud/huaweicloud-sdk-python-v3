# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSnapshotSettingReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bucket': 'str',
        'agency': 'str',
        'base_path': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'agency': 'agency',
        'base_path': 'basePath'
    }

    def __init__(self, bucket=None, agency=None, base_path=None):
        """UpdateSnapshotSettingReq

        The model defined in huaweicloud sdk

        :param bucket: 备份使用的OBS桶的桶名。
        :type bucket: str
        :param agency: 访问OBS使用的IAM委托名称。
        :type agency: str
        :param base_path: 快照在OBS桶中的存放路径。
        :type base_path: str
        """
        
        

        self._bucket = None
        self._agency = None
        self._base_path = None
        self.discriminator = None

        self.bucket = bucket
        self.agency = agency
        self.base_path = base_path

    @property
    def bucket(self):
        """Gets the bucket of this UpdateSnapshotSettingReq.

        备份使用的OBS桶的桶名。

        :return: The bucket of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        """Sets the bucket of this UpdateSnapshotSettingReq.

        备份使用的OBS桶的桶名。

        :param bucket: The bucket of this UpdateSnapshotSettingReq.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def agency(self):
        """Gets the agency of this UpdateSnapshotSettingReq.

        访问OBS使用的IAM委托名称。

        :return: The agency of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        """Sets the agency of this UpdateSnapshotSettingReq.

        访问OBS使用的IAM委托名称。

        :param agency: The agency of this UpdateSnapshotSettingReq.
        :type agency: str
        """
        self._agency = agency

    @property
    def base_path(self):
        """Gets the base_path of this UpdateSnapshotSettingReq.

        快照在OBS桶中的存放路径。

        :return: The base_path of this UpdateSnapshotSettingReq.
        :rtype: str
        """
        return self._base_path

    @base_path.setter
    def base_path(self, base_path):
        """Sets the base_path of this UpdateSnapshotSettingReq.

        快照在OBS桶中的存放路径。

        :param base_path: The base_path of this UpdateSnapshotSettingReq.
        :type base_path: str
        """
        self._base_path = base_path

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
        if not isinstance(other, UpdateSnapshotSettingReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

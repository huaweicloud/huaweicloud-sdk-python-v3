# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupRiskBucketPathResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_domain_id': 'str',
        'bucket_name': 'str',
        'bucket_root_path': 'str'
    }

    attribute_map = {
        'backup_domain_id': 'backup_domain_id',
        'bucket_name': 'bucket_name',
        'bucket_root_path': 'bucket_root_path'
    }

    def __init__(self, backup_domain_id=None, bucket_name=None, bucket_root_path=None):
        r"""ShowBackupRiskBucketPathResponse

        The model defined in huaweicloud sdk

        :param backup_domain_id: 账户ID
        :type backup_domain_id: str
        :param bucket_name: OBS桶名称
        :type bucket_name: str
        :param bucket_root_path: OBS桶根路径
        :type bucket_root_path: str
        """
        
        super(ShowBackupRiskBucketPathResponse, self).__init__()

        self._backup_domain_id = None
        self._bucket_name = None
        self._bucket_root_path = None
        self.discriminator = None

        if backup_domain_id is not None:
            self.backup_domain_id = backup_domain_id
        if bucket_name is not None:
            self.bucket_name = bucket_name
        if bucket_root_path is not None:
            self.bucket_root_path = bucket_root_path

    @property
    def backup_domain_id(self):
        r"""Gets the backup_domain_id of this ShowBackupRiskBucketPathResponse.

        账户ID

        :return: The backup_domain_id of this ShowBackupRiskBucketPathResponse.
        :rtype: str
        """
        return self._backup_domain_id

    @backup_domain_id.setter
    def backup_domain_id(self, backup_domain_id):
        r"""Sets the backup_domain_id of this ShowBackupRiskBucketPathResponse.

        账户ID

        :param backup_domain_id: The backup_domain_id of this ShowBackupRiskBucketPathResponse.
        :type backup_domain_id: str
        """
        self._backup_domain_id = backup_domain_id

    @property
    def bucket_name(self):
        r"""Gets the bucket_name of this ShowBackupRiskBucketPathResponse.

        OBS桶名称

        :return: The bucket_name of this ShowBackupRiskBucketPathResponse.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        r"""Sets the bucket_name of this ShowBackupRiskBucketPathResponse.

        OBS桶名称

        :param bucket_name: The bucket_name of this ShowBackupRiskBucketPathResponse.
        :type bucket_name: str
        """
        self._bucket_name = bucket_name

    @property
    def bucket_root_path(self):
        r"""Gets the bucket_root_path of this ShowBackupRiskBucketPathResponse.

        OBS桶根路径

        :return: The bucket_root_path of this ShowBackupRiskBucketPathResponse.
        :rtype: str
        """
        return self._bucket_root_path

    @bucket_root_path.setter
    def bucket_root_path(self, bucket_root_path):
        r"""Sets the bucket_root_path of this ShowBackupRiskBucketPathResponse.

        OBS桶根路径

        :param bucket_root_path: The bucket_root_path of this ShowBackupRiskBucketPathResponse.
        :type bucket_root_path: str
        """
        self._bucket_root_path = bucket_root_path

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
        if not isinstance(other, ShowBackupRiskBucketPathResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

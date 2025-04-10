# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ObsAuthorityConfig:

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
        'operation': 'int',
        'location': 'str',
        'project_id': 'str'
    }

    attribute_map = {
        'bucket': 'bucket',
        'operation': 'operation',
        'location': 'location',
        'project_id': 'project_id'
    }

    def __init__(self, bucket=None, operation=None, location=None, project_id=None):
        r"""ObsAuthorityConfig

        The model defined in huaweicloud sdk

        :param bucket: OBS桶名
        :type bucket: str
        :param operation: 操作，1-授权；0-取消授权
        :type operation: int
        :param location: 查询bucket所在的region - cn-north-4 - cn-north-1 - cn-north-5 - cn-north-6 - cn-south-1 - cn-east-2
        :type location: str
        :param project_id: 租户华为云账号projectid
        :type project_id: str
        """
        
        

        self._bucket = None
        self._operation = None
        self._location = None
        self._project_id = None
        self.discriminator = None

        self.bucket = bucket
        self.operation = operation
        self.location = location
        if project_id is not None:
            self.project_id = project_id

    @property
    def bucket(self):
        r"""Gets the bucket of this ObsAuthorityConfig.

        OBS桶名

        :return: The bucket of this ObsAuthorityConfig.
        :rtype: str
        """
        return self._bucket

    @bucket.setter
    def bucket(self, bucket):
        r"""Sets the bucket of this ObsAuthorityConfig.

        OBS桶名

        :param bucket: The bucket of this ObsAuthorityConfig.
        :type bucket: str
        """
        self._bucket = bucket

    @property
    def operation(self):
        r"""Gets the operation of this ObsAuthorityConfig.

        操作，1-授权；0-取消授权

        :return: The operation of this ObsAuthorityConfig.
        :rtype: int
        """
        return self._operation

    @operation.setter
    def operation(self, operation):
        r"""Sets the operation of this ObsAuthorityConfig.

        操作，1-授权；0-取消授权

        :param operation: The operation of this ObsAuthorityConfig.
        :type operation: int
        """
        self._operation = operation

    @property
    def location(self):
        r"""Gets the location of this ObsAuthorityConfig.

        查询bucket所在的region - cn-north-4 - cn-north-1 - cn-north-5 - cn-north-6 - cn-south-1 - cn-east-2

        :return: The location of this ObsAuthorityConfig.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ObsAuthorityConfig.

        查询bucket所在的region - cn-north-4 - cn-north-1 - cn-north-5 - cn-north-6 - cn-south-1 - cn-east-2

        :param location: The location of this ObsAuthorityConfig.
        :type location: str
        """
        self._location = location

    @property
    def project_id(self):
        r"""Gets the project_id of this ObsAuthorityConfig.

        租户华为云账号projectid

        :return: The project_id of this ObsAuthorityConfig.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ObsAuthorityConfig.

        租户华为云账号projectid

        :param project_id: The project_id of this ObsAuthorityConfig.
        :type project_id: str
        """
        self._project_id = project_id

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
        if not isinstance(other, ObsAuthorityConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

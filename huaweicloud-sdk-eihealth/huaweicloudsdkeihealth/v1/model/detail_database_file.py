# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetailDatabaseFile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source': 'DatabaseFileSource',
        'url': 'str',
        'eihealth_project_id': 'str',
        'status': 'str',
        'failed_reason': 'str'
    }

    attribute_map = {
        'source': 'source',
        'url': 'url',
        'eihealth_project_id': 'eihealth_project_id',
        'status': 'status',
        'failed_reason': 'failed_reason'
    }

    def __init__(self, source=None, url=None, eihealth_project_id=None, status=None, failed_reason=None):
        r"""DetailDatabaseFile

        The model defined in huaweicloud sdk

        :param source: 
        :type source: :class:`huaweicloudsdkeihealth.v1.DatabaseFileSource`
        :param url: 文件URL，用户私有数据中心为项目路径、公共数据场景为obs地址
        :type url: str
        :param eihealth_project_id: 数据库文件所在项目id，仅文件为数据中心时填写
        :type eihealth_project_id: str
        :param status: 数据库文件写入状态
        :type status: str
        :param failed_reason: 失败原因
        :type failed_reason: str
        """
        
        

        self._source = None
        self._url = None
        self._eihealth_project_id = None
        self._status = None
        self._failed_reason = None
        self.discriminator = None

        self.source = source
        self.url = url
        if eihealth_project_id is not None:
            self.eihealth_project_id = eihealth_project_id
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason

    @property
    def source(self):
        r"""Gets the source of this DetailDatabaseFile.

        :return: The source of this DetailDatabaseFile.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DatabaseFileSource`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this DetailDatabaseFile.

        :param source: The source of this DetailDatabaseFile.
        :type source: :class:`huaweicloudsdkeihealth.v1.DatabaseFileSource`
        """
        self._source = source

    @property
    def url(self):
        r"""Gets the url of this DetailDatabaseFile.

        文件URL，用户私有数据中心为项目路径、公共数据场景为obs地址

        :return: The url of this DetailDatabaseFile.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this DetailDatabaseFile.

        文件URL，用户私有数据中心为项目路径、公共数据场景为obs地址

        :param url: The url of this DetailDatabaseFile.
        :type url: str
        """
        self._url = url

    @property
    def eihealth_project_id(self):
        r"""Gets the eihealth_project_id of this DetailDatabaseFile.

        数据库文件所在项目id，仅文件为数据中心时填写

        :return: The eihealth_project_id of this DetailDatabaseFile.
        :rtype: str
        """
        return self._eihealth_project_id

    @eihealth_project_id.setter
    def eihealth_project_id(self, eihealth_project_id):
        r"""Sets the eihealth_project_id of this DetailDatabaseFile.

        数据库文件所在项目id，仅文件为数据中心时填写

        :param eihealth_project_id: The eihealth_project_id of this DetailDatabaseFile.
        :type eihealth_project_id: str
        """
        self._eihealth_project_id = eihealth_project_id

    @property
    def status(self):
        r"""Gets the status of this DetailDatabaseFile.

        数据库文件写入状态

        :return: The status of this DetailDatabaseFile.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this DetailDatabaseFile.

        数据库文件写入状态

        :param status: The status of this DetailDatabaseFile.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        r"""Gets the failed_reason of this DetailDatabaseFile.

        失败原因

        :return: The failed_reason of this DetailDatabaseFile.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        r"""Sets the failed_reason of this DetailDatabaseFile.

        失败原因

        :param failed_reason: The failed_reason of this DetailDatabaseFile.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

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
        if not isinstance(other, DetailDatabaseFile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

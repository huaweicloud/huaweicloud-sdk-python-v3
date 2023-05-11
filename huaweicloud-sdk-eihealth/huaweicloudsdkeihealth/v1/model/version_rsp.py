# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionRsp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'publisher': 'str',
        'description': 'str',
        'summary': 'str',
        'license': 'str',
        'status': 'str',
        'failed_reason': 'str',
        'labels': 'list[str]',
        'picture': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'version': 'version',
        'publisher': 'publisher',
        'description': 'description',
        'summary': 'summary',
        'license': 'license',
        'status': 'status',
        'failed_reason': 'failed_reason',
        'labels': 'labels',
        'picture': 'picture',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, version=None, publisher=None, description=None, summary=None, license=None, status=None, failed_reason=None, labels=None, picture=None, create_time=None, update_time=None):
        """VersionRsp

        The model defined in huaweicloud sdk

        :param version: 资产版本号
        :type version: str
        :param publisher: 发布者
        :type publisher: str
        :param description: 资产长描述
        :type description: str
        :param summary: 资产短描述
        :type summary: str
        :param license: 许可证
        :type license: str
        :param status: 资产状态
        :type status: str
        :param failed_reason: 资产发布失败原因
        :type failed_reason: str
        :param labels: 资产标签列表
        :type labels: list[str]
        :param picture: 资产封面图访问链接
        :type picture: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._version = None
        self._publisher = None
        self._description = None
        self._summary = None
        self._license = None
        self._status = None
        self._failed_reason = None
        self._labels = None
        self._picture = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if publisher is not None:
            self.publisher = publisher
        if description is not None:
            self.description = description
        if summary is not None:
            self.summary = summary
        if license is not None:
            self.license = license
        if status is not None:
            self.status = status
        if failed_reason is not None:
            self.failed_reason = failed_reason
        if labels is not None:
            self.labels = labels
        if picture is not None:
            self.picture = picture
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def version(self):
        """Gets the version of this VersionRsp.

        资产版本号

        :return: The version of this VersionRsp.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this VersionRsp.

        资产版本号

        :param version: The version of this VersionRsp.
        :type version: str
        """
        self._version = version

    @property
    def publisher(self):
        """Gets the publisher of this VersionRsp.

        发布者

        :return: The publisher of this VersionRsp.
        :rtype: str
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this VersionRsp.

        发布者

        :param publisher: The publisher of this VersionRsp.
        :type publisher: str
        """
        self._publisher = publisher

    @property
    def description(self):
        """Gets the description of this VersionRsp.

        资产长描述

        :return: The description of this VersionRsp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this VersionRsp.

        资产长描述

        :param description: The description of this VersionRsp.
        :type description: str
        """
        self._description = description

    @property
    def summary(self):
        """Gets the summary of this VersionRsp.

        资产短描述

        :return: The summary of this VersionRsp.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this VersionRsp.

        资产短描述

        :param summary: The summary of this VersionRsp.
        :type summary: str
        """
        self._summary = summary

    @property
    def license(self):
        """Gets the license of this VersionRsp.

        许可证

        :return: The license of this VersionRsp.
        :rtype: str
        """
        return self._license

    @license.setter
    def license(self, license):
        """Sets the license of this VersionRsp.

        许可证

        :param license: The license of this VersionRsp.
        :type license: str
        """
        self._license = license

    @property
    def status(self):
        """Gets the status of this VersionRsp.

        资产状态

        :return: The status of this VersionRsp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VersionRsp.

        资产状态

        :param status: The status of this VersionRsp.
        :type status: str
        """
        self._status = status

    @property
    def failed_reason(self):
        """Gets the failed_reason of this VersionRsp.

        资产发布失败原因

        :return: The failed_reason of this VersionRsp.
        :rtype: str
        """
        return self._failed_reason

    @failed_reason.setter
    def failed_reason(self, failed_reason):
        """Sets the failed_reason of this VersionRsp.

        资产发布失败原因

        :param failed_reason: The failed_reason of this VersionRsp.
        :type failed_reason: str
        """
        self._failed_reason = failed_reason

    @property
    def labels(self):
        """Gets the labels of this VersionRsp.

        资产标签列表

        :return: The labels of this VersionRsp.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this VersionRsp.

        资产标签列表

        :param labels: The labels of this VersionRsp.
        :type labels: list[str]
        """
        self._labels = labels

    @property
    def picture(self):
        """Gets the picture of this VersionRsp.

        资产封面图访问链接

        :return: The picture of this VersionRsp.
        :rtype: str
        """
        return self._picture

    @picture.setter
    def picture(self, picture):
        """Sets the picture of this VersionRsp.

        资产封面图访问链接

        :param picture: The picture of this VersionRsp.
        :type picture: str
        """
        self._picture = picture

    @property
    def create_time(self):
        """Gets the create_time of this VersionRsp.

        创建时间

        :return: The create_time of this VersionRsp.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VersionRsp.

        创建时间

        :param create_time: The create_time of this VersionRsp.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this VersionRsp.

        更新时间

        :return: The update_time of this VersionRsp.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this VersionRsp.

        更新时间

        :param update_time: The update_time of this VersionRsp.
        :type update_time: str
        """
        self._update_time = update_time

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
        if not isinstance(other, VersionRsp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

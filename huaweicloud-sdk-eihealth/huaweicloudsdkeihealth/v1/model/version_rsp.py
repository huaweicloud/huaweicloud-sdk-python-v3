# coding: utf-8

import re
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
        'descritpion': 'str',
        'summary': 'str',
        'license': 'str',
        'status': 'str',
        'create_time': 'str',
        'update_time': 'str'
    }

    attribute_map = {
        'version': 'version',
        'publisher': 'publisher',
        'descritpion': 'descritpion',
        'summary': 'summary',
        'license': 'license',
        'status': 'status',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, version=None, publisher=None, descritpion=None, summary=None, license=None, status=None, create_time=None, update_time=None):
        """VersionRsp

        The model defined in huaweicloud sdk

        :param version: 资产版本号
        :type version: str
        :param publisher: 发布者
        :type publisher: str
        :param descritpion: 资产长描述
        :type descritpion: str
        :param summary: 资产短描述
        :type summary: str
        :param license: 许可证
        :type license: str
        :param status: 资产状态
        :type status: str
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 更新时间
        :type update_time: str
        """
        
        

        self._version = None
        self._publisher = None
        self._descritpion = None
        self._summary = None
        self._license = None
        self._status = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if publisher is not None:
            self.publisher = publisher
        if descritpion is not None:
            self.descritpion = descritpion
        if summary is not None:
            self.summary = summary
        if license is not None:
            self.license = license
        if status is not None:
            self.status = status
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
    def descritpion(self):
        """Gets the descritpion of this VersionRsp.

        资产长描述

        :return: The descritpion of this VersionRsp.
        :rtype: str
        """
        return self._descritpion

    @descritpion.setter
    def descritpion(self, descritpion):
        """Sets the descritpion of this VersionRsp.

        资产长描述

        :param descritpion: The descritpion of this VersionRsp.
        :type descritpion: str
        """
        self._descritpion = descritpion

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

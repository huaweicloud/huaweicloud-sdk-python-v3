# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceQuotasInfo:

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
        'total_num': 'int',
        'used_num': 'int',
        'available_num': 'int',
        'available_resources_list': 'list[AvailableResourceIdsInfo]'
    }

    attribute_map = {
        'version': 'version',
        'total_num': 'total_num',
        'used_num': 'used_num',
        'available_num': 'available_num',
        'available_resources_list': 'available_resources_list'
    }

    def __init__(self, version=None, total_num=None, used_num=None, available_num=None, available_resources_list=None):
        """ResourceQuotasInfo

        The model defined in huaweicloud sdk

        :param version: 主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。
        :type version: str
        :param total_num: 总配额数
        :type total_num: int
        :param used_num: 已使用配额数
        :type used_num: int
        :param available_num: 总配额数
        :type available_num: int
        :param available_resources_list: 可用资源列表
        :type available_resources_list: list[:class:`huaweicloudsdkhss.v5.AvailableResourceIdsInfo`]
        """
        
        

        self._version = None
        self._total_num = None
        self._used_num = None
        self._available_num = None
        self._available_resources_list = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if total_num is not None:
            self.total_num = total_num
        if used_num is not None:
            self.used_num = used_num
        if available_num is not None:
            self.available_num = available_num
        if available_resources_list is not None:
            self.available_resources_list = available_resources_list

    @property
    def version(self):
        """Gets the version of this ResourceQuotasInfo.

        主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :return: The version of this ResourceQuotasInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ResourceQuotasInfo.

        主机开通的版本，包含如下6种输入。   - hss.version.null ：无。   - hss.version.basic ：基础版。   - hss.version.enterprise ：企业版。   - hss.version.premium ：旗舰版。   - hss.version.wtp ：网页防篡改版。   - hss.version.container.enterprise：容器版。

        :param version: The version of this ResourceQuotasInfo.
        :type version: str
        """
        self._version = version

    @property
    def total_num(self):
        """Gets the total_num of this ResourceQuotasInfo.

        总配额数

        :return: The total_num of this ResourceQuotasInfo.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ResourceQuotasInfo.

        总配额数

        :param total_num: The total_num of this ResourceQuotasInfo.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def used_num(self):
        """Gets the used_num of this ResourceQuotasInfo.

        已使用配额数

        :return: The used_num of this ResourceQuotasInfo.
        :rtype: int
        """
        return self._used_num

    @used_num.setter
    def used_num(self, used_num):
        """Sets the used_num of this ResourceQuotasInfo.

        已使用配额数

        :param used_num: The used_num of this ResourceQuotasInfo.
        :type used_num: int
        """
        self._used_num = used_num

    @property
    def available_num(self):
        """Gets the available_num of this ResourceQuotasInfo.

        总配额数

        :return: The available_num of this ResourceQuotasInfo.
        :rtype: int
        """
        return self._available_num

    @available_num.setter
    def available_num(self, available_num):
        """Sets the available_num of this ResourceQuotasInfo.

        总配额数

        :param available_num: The available_num of this ResourceQuotasInfo.
        :type available_num: int
        """
        self._available_num = available_num

    @property
    def available_resources_list(self):
        """Gets the available_resources_list of this ResourceQuotasInfo.

        可用资源列表

        :return: The available_resources_list of this ResourceQuotasInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AvailableResourceIdsInfo`]
        """
        return self._available_resources_list

    @available_resources_list.setter
    def available_resources_list(self, available_resources_list):
        """Sets the available_resources_list of this ResourceQuotasInfo.

        可用资源列表

        :param available_resources_list: The available_resources_list of this ResourceQuotasInfo.
        :type available_resources_list: list[:class:`huaweicloudsdkhss.v5.AvailableResourceIdsInfo`]
        """
        self._available_resources_list = available_resources_list

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
        if not isinstance(other, ResourceQuotasInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

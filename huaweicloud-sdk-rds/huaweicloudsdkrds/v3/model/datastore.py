# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Datastore:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'complete_version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'complete_version': 'complete_version'
    }

    def __init__(self, type=None, version=None, complete_version=None):
        """Datastore

        The model defined in huaweicloud sdk

        :param type: 数据库引擎，不区分大小写：  - MySQL - PostgreSQL - SQLServer
        :type type: str
        :param version: 数据库版本。 - MySQL引擎支持5.6、5.7、8.0版本。取值示例：5.7。具有相应权限的用户才可使用8.0，您可联系华为云客服人员申请。 - PostgreSQL引擎支持9.5、9.6、10、11版本。取值示例：9.6。 - Microsoft SQL Server：仅支持2017 企业版、2017 标准版、2017 web版、2014 标准版、2014 企业版、2016 标准版、2016 企业版、2012 企业版、2012 标准版、2012 web版、2008 R2 企业版、2008 R2 web版、2014 web版、2016 web版。取值示例2014_SE。 例如：2017标准版可填写2017_SE，2017企业版可填写2017_EE，2017web版可以填写2017_WEB
        :type version: str
        :param complete_version: 数据库完整版本号。仅在数据库引擎是”PostgreSQL”时返回。
        :type complete_version: str
        """
        
        

        self._type = None
        self._version = None
        self._complete_version = None
        self.discriminator = None

        self.type = type
        self.version = version
        if complete_version is not None:
            self.complete_version = complete_version

    @property
    def type(self):
        """Gets the type of this Datastore.

        数据库引擎，不区分大小写：  - MySQL - PostgreSQL - SQLServer

        :return: The type of this Datastore.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Datastore.

        数据库引擎，不区分大小写：  - MySQL - PostgreSQL - SQLServer

        :param type: The type of this Datastore.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this Datastore.

        数据库版本。 - MySQL引擎支持5.6、5.7、8.0版本。取值示例：5.7。具有相应权限的用户才可使用8.0，您可联系华为云客服人员申请。 - PostgreSQL引擎支持9.5、9.6、10、11版本。取值示例：9.6。 - Microsoft SQL Server：仅支持2017 企业版、2017 标准版、2017 web版、2014 标准版、2014 企业版、2016 标准版、2016 企业版、2012 企业版、2012 标准版、2012 web版、2008 R2 企业版、2008 R2 web版、2014 web版、2016 web版。取值示例2014_SE。 例如：2017标准版可填写2017_SE，2017企业版可填写2017_EE，2017web版可以填写2017_WEB

        :return: The version of this Datastore.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Datastore.

        数据库版本。 - MySQL引擎支持5.6、5.7、8.0版本。取值示例：5.7。具有相应权限的用户才可使用8.0，您可联系华为云客服人员申请。 - PostgreSQL引擎支持9.5、9.6、10、11版本。取值示例：9.6。 - Microsoft SQL Server：仅支持2017 企业版、2017 标准版、2017 web版、2014 标准版、2014 企业版、2016 标准版、2016 企业版、2012 企业版、2012 标准版、2012 web版、2008 R2 企业版、2008 R2 web版、2014 web版、2016 web版。取值示例2014_SE。 例如：2017标准版可填写2017_SE，2017企业版可填写2017_EE，2017web版可以填写2017_WEB

        :param version: The version of this Datastore.
        :type version: str
        """
        self._version = version

    @property
    def complete_version(self):
        """Gets the complete_version of this Datastore.

        数据库完整版本号。仅在数据库引擎是”PostgreSQL”时返回。

        :return: The complete_version of this Datastore.
        :rtype: str
        """
        return self._complete_version

    @complete_version.setter
    def complete_version(self, complete_version):
        """Sets the complete_version of this Datastore.

        数据库完整版本号。仅在数据库引擎是”PostgreSQL”时返回。

        :param complete_version: The complete_version of this Datastore.
        :type complete_version: str
        """
        self._complete_version = complete_version

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
        if not isinstance(other, Datastore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

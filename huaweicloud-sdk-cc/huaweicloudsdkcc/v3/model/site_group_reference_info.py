# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SiteGroupReferenceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'description': 'str',
        'name_en': 'str',
        'name_cn': 'str'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'name_en': 'name_en',
        'name_cn': 'name_cn'
    }

    def __init__(self, id=None, description=None, name_en=None, name_cn=None):
        r"""SiteGroupReferenceInfo

        The model defined in huaweicloud sdk

        :param id: 实例ID。
        :type id: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param name_en: 功能说明：站点分组自定义的英文名字。 取值范围：1-255个字符。
        :type name_en: str
        :param name_cn: 功能说明：站点分组自定义的中文名字。 取值范围：1-64个字符。
        :type name_cn: str
        """
        
        

        self._id = None
        self._description = None
        self._name_en = None
        self._name_cn = None
        self.discriminator = None

        self.id = id
        if description is not None:
            self.description = description
        if name_en is not None:
            self.name_en = name_en
        if name_cn is not None:
            self.name_cn = name_cn

    @property
    def id(self):
        r"""Gets the id of this SiteGroupReferenceInfo.

        实例ID。

        :return: The id of this SiteGroupReferenceInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SiteGroupReferenceInfo.

        实例ID。

        :param id: The id of this SiteGroupReferenceInfo.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this SiteGroupReferenceInfo.

        实例描述。不支持 <>。

        :return: The description of this SiteGroupReferenceInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this SiteGroupReferenceInfo.

        实例描述。不支持 <>。

        :param description: The description of this SiteGroupReferenceInfo.
        :type description: str
        """
        self._description = description

    @property
    def name_en(self):
        r"""Gets the name_en of this SiteGroupReferenceInfo.

        功能说明：站点分组自定义的英文名字。 取值范围：1-255个字符。

        :return: The name_en of this SiteGroupReferenceInfo.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this SiteGroupReferenceInfo.

        功能说明：站点分组自定义的英文名字。 取值范围：1-255个字符。

        :param name_en: The name_en of this SiteGroupReferenceInfo.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def name_cn(self):
        r"""Gets the name_cn of this SiteGroupReferenceInfo.

        功能说明：站点分组自定义的中文名字。 取值范围：1-64个字符。

        :return: The name_cn of this SiteGroupReferenceInfo.
        :rtype: str
        """
        return self._name_cn

    @name_cn.setter
    def name_cn(self, name_cn):
        r"""Sets the name_cn of this SiteGroupReferenceInfo.

        功能说明：站点分组自定义的中文名字。 取值范围：1-64个字符。

        :param name_cn: The name_cn of this SiteGroupReferenceInfo.
        :type name_cn: str
        """
        self._name_cn = name_cn

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
        if not isinstance(other, SiteGroupReferenceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

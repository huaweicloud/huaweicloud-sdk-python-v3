# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomTemplates:

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
        'name': 'str',
        'conf_content': 'str',
        'desc': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'conf_content': 'confContent',
        'desc': 'desc'
    }

    def __init__(self, id=None, name=None, conf_content=None, desc=None):
        r"""CustomTemplates

        The model defined in huaweicloud sdk

        :param id: 配置文件id。
        :type id: str
        :param name: 配置文件名称。
        :type name: str
        :param conf_content: 配置文件内容。
        :type conf_content: str
        :param desc: 描述。
        :type desc: str
        """
        
        

        self._id = None
        self._name = None
        self._conf_content = None
        self._desc = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if conf_content is not None:
            self.conf_content = conf_content
        if desc is not None:
            self.desc = desc

    @property
    def id(self):
        r"""Gets the id of this CustomTemplates.

        配置文件id。

        :return: The id of this CustomTemplates.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CustomTemplates.

        配置文件id。

        :param id: The id of this CustomTemplates.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this CustomTemplates.

        配置文件名称。

        :return: The name of this CustomTemplates.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomTemplates.

        配置文件名称。

        :param name: The name of this CustomTemplates.
        :type name: str
        """
        self._name = name

    @property
    def conf_content(self):
        r"""Gets the conf_content of this CustomTemplates.

        配置文件内容。

        :return: The conf_content of this CustomTemplates.
        :rtype: str
        """
        return self._conf_content

    @conf_content.setter
    def conf_content(self, conf_content):
        r"""Sets the conf_content of this CustomTemplates.

        配置文件内容。

        :param conf_content: The conf_content of this CustomTemplates.
        :type conf_content: str
        """
        self._conf_content = conf_content

    @property
    def desc(self):
        r"""Gets the desc of this CustomTemplates.

        描述。

        :return: The desc of this CustomTemplates.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this CustomTemplates.

        描述。

        :param desc: The desc of this CustomTemplates.
        :type desc: str
        """
        self._desc = desc

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
        if not isinstance(other, CustomTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

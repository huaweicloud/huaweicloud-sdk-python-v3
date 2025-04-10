# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTemplate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'is_servicestage': 'int',
        'desc': 'str',
        'obs_url': 'str',
        'tags': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'is_servicestage': 'is_servicestage',
        'desc': 'desc',
        'obs_url': 'obs_url',
        'tags': 'tags'
    }

    def __init__(self, name=None, is_servicestage=None, desc=None, obs_url=None, tags=None):
        r"""CreateTemplate

        The model defined in huaweicloud sdk

        :param name: 模板名称,必填
        :type name: str
        :param is_servicestage: 应用是否托管到servicestage,1是托管,0是不托管,非必填
        :type is_servicestage: int
        :param desc: 描述信息,非必填
        :type desc: str
        :param obs_url: 模板在桶中的url,必填
        :type obs_url: str
        :param tags: 模板标签,非必填
        :type tags: list[str]
        """
        
        

        self._name = None
        self._is_servicestage = None
        self._desc = None
        self._obs_url = None
        self._tags = None
        self.discriminator = None

        self.name = name
        if is_servicestage is not None:
            self.is_servicestage = is_servicestage
        if desc is not None:
            self.desc = desc
        self.obs_url = obs_url
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateTemplate.

        模板名称,必填

        :return: The name of this CreateTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTemplate.

        模板名称,必填

        :param name: The name of this CreateTemplate.
        :type name: str
        """
        self._name = name

    @property
    def is_servicestage(self):
        r"""Gets the is_servicestage of this CreateTemplate.

        应用是否托管到servicestage,1是托管,0是不托管,非必填

        :return: The is_servicestage of this CreateTemplate.
        :rtype: int
        """
        return self._is_servicestage

    @is_servicestage.setter
    def is_servicestage(self, is_servicestage):
        r"""Sets the is_servicestage of this CreateTemplate.

        应用是否托管到servicestage,1是托管,0是不托管,非必填

        :param is_servicestage: The is_servicestage of this CreateTemplate.
        :type is_servicestage: int
        """
        self._is_servicestage = is_servicestage

    @property
    def desc(self):
        r"""Gets the desc of this CreateTemplate.

        描述信息,非必填

        :return: The desc of this CreateTemplate.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this CreateTemplate.

        描述信息,非必填

        :param desc: The desc of this CreateTemplate.
        :type desc: str
        """
        self._desc = desc

    @property
    def obs_url(self):
        r"""Gets the obs_url of this CreateTemplate.

        模板在桶中的url,必填

        :return: The obs_url of this CreateTemplate.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        r"""Sets the obs_url of this CreateTemplate.

        模板在桶中的url,必填

        :param obs_url: The obs_url of this CreateTemplate.
        :type obs_url: str
        """
        self._obs_url = obs_url

    @property
    def tags(self):
        r"""Gets the tags of this CreateTemplate.

        模板标签,非必填

        :return: The tags of this CreateTemplate.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateTemplate.

        模板标签,非必填

        :param tags: The tags of this CreateTemplate.
        :type tags: list[str]
        """
        self._tags = tags

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
        if not isinstance(other, CreateTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

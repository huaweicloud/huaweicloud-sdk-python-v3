# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTemplates:

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
        'description': 'str',
        'tags': 'list[str]',
        'status': 'int',
        'obs_url': 'str',
        'is_servicestage': 'int'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'tags': 'tags',
        'status': 'status',
        'obs_url': 'obs_url',
        'is_servicestage': 'is_servicestage'
    }

    def __init__(self, name=None, description=None, tags=None, status=None, obs_url=None, is_servicestage=None):
        """UpdateTemplates

        The model defined in huaweicloud sdk

        :param name: 模板名称,非必填
        :type name: str
        :param description: 模板描述,非必填
        :type description: str
        :param tags: 模板标签,非必填
        :type tags: list[str]
        :param status: 模板状态,非必填
        :type status: int
        :param obs_url: obs地址,必填
        :type obs_url: str
        :param is_servicestage: 应用是否托管到servicestage,1是托管,0是不托管,非必填
        :type is_servicestage: int
        """
        
        

        self._name = None
        self._description = None
        self._tags = None
        self._status = None
        self._obs_url = None
        self._is_servicestage = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status
        if obs_url is not None:
            self.obs_url = obs_url
        if is_servicestage is not None:
            self.is_servicestage = is_servicestage

    @property
    def name(self):
        """Gets the name of this UpdateTemplates.

        模板名称,非必填

        :return: The name of this UpdateTemplates.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateTemplates.

        模板名称,非必填

        :param name: The name of this UpdateTemplates.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateTemplates.

        模板描述,非必填

        :return: The description of this UpdateTemplates.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateTemplates.

        模板描述,非必填

        :param description: The description of this UpdateTemplates.
        :type description: str
        """
        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UpdateTemplates.

        模板标签,非必填

        :return: The tags of this UpdateTemplates.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateTemplates.

        模板标签,非必填

        :param tags: The tags of this UpdateTemplates.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def status(self):
        """Gets the status of this UpdateTemplates.

        模板状态,非必填

        :return: The status of this UpdateTemplates.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateTemplates.

        模板状态,非必填

        :param status: The status of this UpdateTemplates.
        :type status: int
        """
        self._status = status

    @property
    def obs_url(self):
        """Gets the obs_url of this UpdateTemplates.

        obs地址,必填

        :return: The obs_url of this UpdateTemplates.
        :rtype: str
        """
        return self._obs_url

    @obs_url.setter
    def obs_url(self, obs_url):
        """Sets the obs_url of this UpdateTemplates.

        obs地址,必填

        :param obs_url: The obs_url of this UpdateTemplates.
        :type obs_url: str
        """
        self._obs_url = obs_url

    @property
    def is_servicestage(self):
        """Gets the is_servicestage of this UpdateTemplates.

        应用是否托管到servicestage,1是托管,0是不托管,非必填

        :return: The is_servicestage of this UpdateTemplates.
        :rtype: int
        """
        return self._is_servicestage

    @is_servicestage.setter
    def is_servicestage(self, is_servicestage):
        """Sets the is_servicestage of this UpdateTemplates.

        应用是否托管到servicestage,1是托管,0是不托管,非必填

        :param is_servicestage: The is_servicestage of this UpdateTemplates.
        :type is_servicestage: int
        """
        self._is_servicestage = is_servicestage

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
        if not isinstance(other, UpdateTemplates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

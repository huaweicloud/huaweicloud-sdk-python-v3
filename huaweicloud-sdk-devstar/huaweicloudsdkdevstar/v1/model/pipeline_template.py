# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PipelineTemplate:

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
        'id': 'str',
        'description': 'str',
        'region_id': 'str',
        'url': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'region_id': 'region_id',
        'url': 'url'
    }

    def __init__(self, name=None, id=None, description=None, region_id=None, url=None):
        """PipelineTemplate

        The model defined in huaweicloud sdk

        :param name: 模板名称
        :type name: str
        :param id: 模板id
        :type id: str
        :param description: 描述信息
        :type description: str
        :param region_id: 区域id
        :type region_id: str
        :param url: 预览链接
        :type url: str
        """
        
        

        self._name = None
        self._id = None
        self._description = None
        self._region_id = None
        self._url = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if region_id is not None:
            self.region_id = region_id
        if url is not None:
            self.url = url

    @property
    def name(self):
        """Gets the name of this PipelineTemplate.

        模板名称

        :return: The name of this PipelineTemplate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PipelineTemplate.

        模板名称

        :param name: The name of this PipelineTemplate.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this PipelineTemplate.

        模板id

        :return: The id of this PipelineTemplate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PipelineTemplate.

        模板id

        :param id: The id of this PipelineTemplate.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        """Gets the description of this PipelineTemplate.

        描述信息

        :return: The description of this PipelineTemplate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PipelineTemplate.

        描述信息

        :param description: The description of this PipelineTemplate.
        :type description: str
        """
        self._description = description

    @property
    def region_id(self):
        """Gets the region_id of this PipelineTemplate.

        区域id

        :return: The region_id of this PipelineTemplate.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this PipelineTemplate.

        区域id

        :param region_id: The region_id of this PipelineTemplate.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def url(self):
        """Gets the url of this PipelineTemplate.

        预览链接

        :return: The url of this PipelineTemplate.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PipelineTemplate.

        预览链接

        :param url: The url of this PipelineTemplate.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, PipelineTemplate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

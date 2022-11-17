# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProjectReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'status': 'ProjectStatus',
        'tags': 'list[str]',
        'is_core': 'bool'
    }

    attribute_map = {
        'description': 'description',
        'status': 'status',
        'tags': 'tags',
        'is_core': 'is_core'
    }

    def __init__(self, description=None, status=None, tags=None, is_core=None):
        """UpdateProjectReq

        The model defined in huaweicloud sdk

        :param description: 项目描述
        :type description: str
        :param status: 
        :type status: :class:`huaweicloudsdkeihealth.v1.ProjectStatus`
        :param tags: 项目标签
        :type tags: list[str]
        :param is_core: 是否为核心项目标记
        :type is_core: bool
        """
        
        

        self._description = None
        self._status = None
        self._tags = None
        self._is_core = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if tags is not None:
            self.tags = tags
        if is_core is not None:
            self.is_core = is_core

    @property
    def description(self):
        """Gets the description of this UpdateProjectReq.

        项目描述

        :return: The description of this UpdateProjectReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateProjectReq.

        项目描述

        :param description: The description of this UpdateProjectReq.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        """Gets the status of this UpdateProjectReq.

        :return: The status of this UpdateProjectReq.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ProjectStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateProjectReq.

        :param status: The status of this UpdateProjectReq.
        :type status: :class:`huaweicloudsdkeihealth.v1.ProjectStatus`
        """
        self._status = status

    @property
    def tags(self):
        """Gets the tags of this UpdateProjectReq.

        项目标签

        :return: The tags of this UpdateProjectReq.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateProjectReq.

        项目标签

        :param tags: The tags of this UpdateProjectReq.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def is_core(self):
        """Gets the is_core of this UpdateProjectReq.

        是否为核心项目标记

        :return: The is_core of this UpdateProjectReq.
        :rtype: bool
        """
        return self._is_core

    @is_core.setter
    def is_core(self, is_core):
        """Sets the is_core of this UpdateProjectReq.

        是否为核心项目标记

        :param is_core: The is_core of this UpdateProjectReq.
        :type is_core: bool
        """
        self._is_core = is_core

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
        if not isinstance(other, UpdateProjectReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

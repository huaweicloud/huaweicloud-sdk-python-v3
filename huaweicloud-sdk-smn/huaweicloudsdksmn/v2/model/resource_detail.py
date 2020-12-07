# coding: utf-8

import pprint
import re

import six





class ResourceDetail:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'detail_id': 'str',
        'topic_urn': 'str',
        'display_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'detail_id': 'detailId',
        'topic_urn': 'topic_urn',
        'display_name': 'display_name'
    }

    def __init__(self, enterprise_project_id=None, detail_id=None, topic_urn=None, display_name=None):
        """ResourceDetail - a model defined in huaweicloud sdk"""
        
        

        self._enterprise_project_id = None
        self._detail_id = None
        self._topic_urn = None
        self._display_name = None
        self.discriminator = None

        self.enterprise_project_id = enterprise_project_id
        self.detail_id = detail_id
        self.topic_urn = topic_urn
        self.display_name = display_name

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ResourceDetail.

        企业项目ID

        :return: The enterprise_project_id of this ResourceDetail.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ResourceDetail.

        企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ResourceDetail.
        :type: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def detail_id(self):
        """Gets the detail_id of this ResourceDetail.

        详情ID

        :return: The detail_id of this ResourceDetail.
        :rtype: str
        """
        return self._detail_id

    @detail_id.setter
    def detail_id(self, detail_id):
        """Sets the detail_id of this ResourceDetail.

        详情ID

        :param detail_id: The detail_id of this ResourceDetail.
        :type: str
        """
        self._detail_id = detail_id

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ResourceDetail.

        topic唯一标识

        :return: The topic_urn of this ResourceDetail.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ResourceDetail.

        topic唯一标识

        :param topic_urn: The topic_urn of this ResourceDetail.
        :type: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        """Gets the display_name of this ResourceDetail.

        显示名

        :return: The display_name of this ResourceDetail.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ResourceDetail.

        显示名

        :param display_name: The display_name of this ResourceDetail.
        :type: str
        """
        self._display_name = display_name

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ResourceDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

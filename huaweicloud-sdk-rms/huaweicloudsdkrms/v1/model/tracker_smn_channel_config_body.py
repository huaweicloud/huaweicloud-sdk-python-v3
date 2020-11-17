# coding: utf-8

import pprint
import re

import six





class TrackerSMNChannelConfigBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'region_id': 'str',
        'project_id': 'str',
        'topic_urn': 'str'
    }

    attribute_map = {
        'region_id': 'region_id',
        'project_id': 'project_id',
        'topic_urn': 'topic_urn'
    }

    def __init__(self, region_id=None, project_id=None, topic_urn=None):
        """TrackerSMNChannelConfigBody - a model defined in huaweicloud sdk"""
        
        

        self._region_id = None
        self._project_id = None
        self._topic_urn = None
        self.discriminator = None

        self.region_id = region_id
        self.project_id = project_id
        self.topic_urn = topic_urn

    @property
    def region_id(self):
        """Gets the region_id of this TrackerSMNChannelConfigBody.

        region id

        :return: The region_id of this TrackerSMNChannelConfigBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this TrackerSMNChannelConfigBody.

        region id

        :param region_id: The region_id of this TrackerSMNChannelConfigBody.
        :type: str
        """
        self._region_id = region_id

    @property
    def project_id(self):
        """Gets the project_id of this TrackerSMNChannelConfigBody.

        project id

        :return: The project_id of this TrackerSMNChannelConfigBody.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TrackerSMNChannelConfigBody.

        project id

        :param project_id: The project_id of this TrackerSMNChannelConfigBody.
        :type: str
        """
        self._project_id = project_id

    @property
    def topic_urn(self):
        """Gets the topic_urn of this TrackerSMNChannelConfigBody.

        SMN 主题urn

        :return: The topic_urn of this TrackerSMNChannelConfigBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this TrackerSMNChannelConfigBody.

        SMN 主题urn

        :param topic_urn: The topic_urn of this TrackerSMNChannelConfigBody.
        :type: str
        """
        self._topic_urn = topic_urn

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
        if not isinstance(other, TrackerSMNChannelConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListAlarmTemplatesResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'alarm_templates': 'list[AlarmTemplate]',
        'meta_data': 'MetaData'
    }

    attribute_map = {
        'alarm_templates': 'alarm_templates',
        'meta_data': 'meta_data'
    }

    def __init__(self, alarm_templates=None, meta_data=None):
        """ListAlarmTemplatesResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._alarm_templates = None
        self._meta_data = None
        self.discriminator = None

        if alarm_templates is not None:
            self.alarm_templates = alarm_templates
        if meta_data is not None:
            self.meta_data = meta_data

    @property
    def alarm_templates(self):
        """Gets the alarm_templates of this ListAlarmTemplatesResponse.

        自定义告警模板详细信息。

        :return: The alarm_templates of this ListAlarmTemplatesResponse.
        :rtype: list[AlarmTemplate]
        """
        return self._alarm_templates

    @alarm_templates.setter
    def alarm_templates(self, alarm_templates):
        """Sets the alarm_templates of this ListAlarmTemplatesResponse.

        自定义告警模板详细信息。

        :param alarm_templates: The alarm_templates of this ListAlarmTemplatesResponse.
        :type: list[AlarmTemplate]
        """
        self._alarm_templates = alarm_templates

    @property
    def meta_data(self):
        """Gets the meta_data of this ListAlarmTemplatesResponse.


        :return: The meta_data of this ListAlarmTemplatesResponse.
        :rtype: MetaData
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this ListAlarmTemplatesResponse.


        :param meta_data: The meta_data of this ListAlarmTemplatesResponse.
        :type: MetaData
        """
        self._meta_data = meta_data

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
        if not isinstance(other, ListAlarmTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateSrcReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_template_id': 'str',
        'destination_template_name': 'str'
    }

    attribute_map = {
        'source_template_id': 'source_template_id',
        'destination_template_name': 'destination_template_name'
    }

    def __init__(self, source_template_id=None, destination_template_name=None):
        """TemplateSrcReq

        The model defined in huaweicloud sdk

        :param source_template_id: 源模板id
        :type source_template_id: str
        :param destination_template_name: 导入模板名称
        :type destination_template_name: str
        """
        
        

        self._source_template_id = None
        self._destination_template_name = None
        self.discriminator = None

        self.source_template_id = source_template_id
        self.destination_template_name = destination_template_name

    @property
    def source_template_id(self):
        """Gets the source_template_id of this TemplateSrcReq.

        源模板id

        :return: The source_template_id of this TemplateSrcReq.
        :rtype: str
        """
        return self._source_template_id

    @source_template_id.setter
    def source_template_id(self, source_template_id):
        """Sets the source_template_id of this TemplateSrcReq.

        源模板id

        :param source_template_id: The source_template_id of this TemplateSrcReq.
        :type source_template_id: str
        """
        self._source_template_id = source_template_id

    @property
    def destination_template_name(self):
        """Gets the destination_template_name of this TemplateSrcReq.

        导入模板名称

        :return: The destination_template_name of this TemplateSrcReq.
        :rtype: str
        """
        return self._destination_template_name

    @destination_template_name.setter
    def destination_template_name(self, destination_template_name):
        """Sets the destination_template_name of this TemplateSrcReq.

        导入模板名称

        :param destination_template_name: The destination_template_name of this TemplateSrcReq.
        :type destination_template_name: str
        """
        self._destination_template_name = destination_template_name

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
        if not isinstance(other, TemplateSrcReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

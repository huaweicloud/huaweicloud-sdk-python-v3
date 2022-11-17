# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDefectRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'defect_id': 'str',
        'defect_status': 'str'
    }

    attribute_map = {
        'defect_id': 'defect_id',
        'defect_status': 'defect_status'
    }

    def __init__(self, defect_id=None, defect_status=None):
        """UpdateDefectRequestBody

        The model defined in huaweicloud sdk

        :param defect_id: 问题id,多个时英文逗号分隔
        :type defect_id: str
        :param defect_status: 状态2：已忽略 1：已解决 0：未解决
        :type defect_status: str
        """
        
        

        self._defect_id = None
        self._defect_status = None
        self.discriminator = None

        if defect_id is not None:
            self.defect_id = defect_id
        if defect_status is not None:
            self.defect_status = defect_status

    @property
    def defect_id(self):
        """Gets the defect_id of this UpdateDefectRequestBody.

        问题id,多个时英文逗号分隔

        :return: The defect_id of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._defect_id

    @defect_id.setter
    def defect_id(self, defect_id):
        """Sets the defect_id of this UpdateDefectRequestBody.

        问题id,多个时英文逗号分隔

        :param defect_id: The defect_id of this UpdateDefectRequestBody.
        :type defect_id: str
        """
        self._defect_id = defect_id

    @property
    def defect_status(self):
        """Gets the defect_status of this UpdateDefectRequestBody.

        状态2：已忽略 1：已解决 0：未解决

        :return: The defect_status of this UpdateDefectRequestBody.
        :rtype: str
        """
        return self._defect_status

    @defect_status.setter
    def defect_status(self, defect_status):
        """Sets the defect_status of this UpdateDefectRequestBody.

        状态2：已忽略 1：已解决 0：未解决

        :param defect_status: The defect_status of this UpdateDefectRequestBody.
        :type defect_status: str
        """
        self._defect_status = defect_status

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
        if not isinstance(other, UpdateDefectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

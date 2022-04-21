# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiQuantitiesV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'instance_num': 'int',
        'nums_on_release': 'int',
        'nums_off_release': 'int'
    }

    attribute_map = {
        'instance_num': 'instance_num',
        'nums_on_release': 'nums_on_release',
        'nums_off_release': 'nums_off_release'
    }

    def __init__(self, instance_num=None, nums_on_release=None, nums_off_release=None):
        """ListApiQuantitiesV2Response

        The model defined in huaweicloud sdk

        :param instance_num: API总个数
        :type instance_num: int
        :param nums_on_release: 已发布到release环境的API个数
        :type nums_on_release: int
        :param nums_off_release: 未发布到release环境的API个数
        :type nums_off_release: int
        """
        
        super(ListApiQuantitiesV2Response, self).__init__()

        self._instance_num = None
        self._nums_on_release = None
        self._nums_off_release = None
        self.discriminator = None

        if instance_num is not None:
            self.instance_num = instance_num
        if nums_on_release is not None:
            self.nums_on_release = nums_on_release
        if nums_off_release is not None:
            self.nums_off_release = nums_off_release

    @property
    def instance_num(self):
        """Gets the instance_num of this ListApiQuantitiesV2Response.

        API总个数

        :return: The instance_num of this ListApiQuantitiesV2Response.
        :rtype: int
        """
        return self._instance_num

    @instance_num.setter
    def instance_num(self, instance_num):
        """Sets the instance_num of this ListApiQuantitiesV2Response.

        API总个数

        :param instance_num: The instance_num of this ListApiQuantitiesV2Response.
        :type instance_num: int
        """
        self._instance_num = instance_num

    @property
    def nums_on_release(self):
        """Gets the nums_on_release of this ListApiQuantitiesV2Response.

        已发布到release环境的API个数

        :return: The nums_on_release of this ListApiQuantitiesV2Response.
        :rtype: int
        """
        return self._nums_on_release

    @nums_on_release.setter
    def nums_on_release(self, nums_on_release):
        """Sets the nums_on_release of this ListApiQuantitiesV2Response.

        已发布到release环境的API个数

        :param nums_on_release: The nums_on_release of this ListApiQuantitiesV2Response.
        :type nums_on_release: int
        """
        self._nums_on_release = nums_on_release

    @property
    def nums_off_release(self):
        """Gets the nums_off_release of this ListApiQuantitiesV2Response.

        未发布到release环境的API个数

        :return: The nums_off_release of this ListApiQuantitiesV2Response.
        :rtype: int
        """
        return self._nums_off_release

    @nums_off_release.setter
    def nums_off_release(self, nums_off_release):
        """Sets the nums_off_release of this ListApiQuantitiesV2Response.

        未发布到release环境的API个数

        :param nums_off_release: The nums_off_release of this ListApiQuantitiesV2Response.
        :type nums_off_release: int
        """
        self._nums_off_release = nums_off_release

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
        if not isinstance(other, ListApiQuantitiesV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

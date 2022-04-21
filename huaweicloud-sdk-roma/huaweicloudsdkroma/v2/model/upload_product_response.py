# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadProductResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'succ_num': 'int',
        'fail_num': 'int',
        'fail_objects_ids': 'list[str]'
    }

    attribute_map = {
        'succ_num': 'succ_num',
        'fail_num': 'fail_num',
        'fail_objects_ids': 'fail_objects_ids'
    }

    def __init__(self, succ_num=None, fail_num=None, fail_objects_ids=None):
        """UploadProductResponse

        The model defined in huaweicloud sdk

        :param succ_num: 导入成功的产品数
        :type succ_num: int
        :param fail_num: 导入失败的产品数
        :type fail_num: int
        :param fail_objects_ids: 导入失败的产品名称列表
        :type fail_objects_ids: list[str]
        """
        
        super(UploadProductResponse, self).__init__()

        self._succ_num = None
        self._fail_num = None
        self._fail_objects_ids = None
        self.discriminator = None

        if succ_num is not None:
            self.succ_num = succ_num
        if fail_num is not None:
            self.fail_num = fail_num
        if fail_objects_ids is not None:
            self.fail_objects_ids = fail_objects_ids

    @property
    def succ_num(self):
        """Gets the succ_num of this UploadProductResponse.

        导入成功的产品数

        :return: The succ_num of this UploadProductResponse.
        :rtype: int
        """
        return self._succ_num

    @succ_num.setter
    def succ_num(self, succ_num):
        """Sets the succ_num of this UploadProductResponse.

        导入成功的产品数

        :param succ_num: The succ_num of this UploadProductResponse.
        :type succ_num: int
        """
        self._succ_num = succ_num

    @property
    def fail_num(self):
        """Gets the fail_num of this UploadProductResponse.

        导入失败的产品数

        :return: The fail_num of this UploadProductResponse.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        """Sets the fail_num of this UploadProductResponse.

        导入失败的产品数

        :param fail_num: The fail_num of this UploadProductResponse.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def fail_objects_ids(self):
        """Gets the fail_objects_ids of this UploadProductResponse.

        导入失败的产品名称列表

        :return: The fail_objects_ids of this UploadProductResponse.
        :rtype: list[str]
        """
        return self._fail_objects_ids

    @fail_objects_ids.setter
    def fail_objects_ids(self, fail_objects_ids):
        """Sets the fail_objects_ids of this UploadProductResponse.

        导入失败的产品名称列表

        :param fail_objects_ids: The fail_objects_ids of this UploadProductResponse.
        :type fail_objects_ids: list[str]
        """
        self._fail_objects_ids = fail_objects_ids

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
        if not isinstance(other, UploadProductResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

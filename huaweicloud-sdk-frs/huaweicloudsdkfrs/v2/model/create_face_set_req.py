# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateFaceSetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_fields': 'dict(str, TypeInfo)',
        'face_set_name': 'str',
        'face_set_capacity': 'int'
    }

    attribute_map = {
        'external_fields': 'external_fields',
        'face_set_name': 'face_set_name',
        'face_set_capacity': 'face_set_capacity'
    }

    def __init__(self, external_fields=None, face_set_name=None, face_set_capacity=None):
        r"""CreateFaceSetReq

        The model defined in huaweicloud sdk

        :param external_fields: 用户自定义数据，自定义字段不能以系统保留字段vector、bounding_box、external_image_id、face_id、create_time、_id、_all、_source等字段命名。Json字符串不校验重复性，自定义字段的key值长度范围为[1,36]，string类型的value长度范围为[1,256]，具体参见[[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)。](tag:hc) [[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)。](tag:hk)
        :type external_fields: dict(str, TypeInfo)
        :param face_set_name: 人脸库名称。 建议人脸库的名称不要以下划线（_）开头，否则云监控服务会无法采集人脸数量。
        :type face_set_name: str
        :param face_set_capacity: 人脸库最大的容量，填写1万整数倍的数字，例如：30000。 默认为100000，最大值为100000，可通过创建新的人脸库进行扩容，每个用户可免费默认使用10个人脸库，每个人脸库容量为10万个人脸特征。如需扩容单个人脸库规模，请联系华为云客服确认扩容规模与价格。
        :type face_set_capacity: int
        """
        
        

        self._external_fields = None
        self._face_set_name = None
        self._face_set_capacity = None
        self.discriminator = None

        if external_fields is not None:
            self.external_fields = external_fields
        self.face_set_name = face_set_name
        if face_set_capacity is not None:
            self.face_set_capacity = face_set_capacity

    @property
    def external_fields(self):
        r"""Gets the external_fields of this CreateFaceSetReq.

        用户自定义数据，自定义字段不能以系统保留字段vector、bounding_box、external_image_id、face_id、create_time、_id、_all、_source等字段命名。Json字符串不校验重复性，自定义字段的key值长度范围为[1,36]，string类型的value长度范围为[1,256]，具体参见[[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)。](tag:hc) [[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)。](tag:hk)

        :return: The external_fields of this CreateFaceSetReq.
        :rtype: dict(str, TypeInfo)
        """
        return self._external_fields

    @external_fields.setter
    def external_fields(self, external_fields):
        r"""Sets the external_fields of this CreateFaceSetReq.

        用户自定义数据，自定义字段不能以系统保留字段vector、bounding_box、external_image_id、face_id、create_time、_id、_all、_source等字段命名。Json字符串不校验重复性，自定义字段的key值长度范围为[1,36]，string类型的value长度范围为[1,256]，具体参见[[自定义字段](https://support.huaweicloud.com/api-face/face_02_0012.html)。](tag:hc) [[自定义字段](https://support.huaweicloud.com/intl/zh-cn/api-face/face_02_0012.html)。](tag:hk)

        :param external_fields: The external_fields of this CreateFaceSetReq.
        :type external_fields: dict(str, TypeInfo)
        """
        self._external_fields = external_fields

    @property
    def face_set_name(self):
        r"""Gets the face_set_name of this CreateFaceSetReq.

        人脸库名称。 建议人脸库的名称不要以下划线（_）开头，否则云监控服务会无法采集人脸数量。

        :return: The face_set_name of this CreateFaceSetReq.
        :rtype: str
        """
        return self._face_set_name

    @face_set_name.setter
    def face_set_name(self, face_set_name):
        r"""Sets the face_set_name of this CreateFaceSetReq.

        人脸库名称。 建议人脸库的名称不要以下划线（_）开头，否则云监控服务会无法采集人脸数量。

        :param face_set_name: The face_set_name of this CreateFaceSetReq.
        :type face_set_name: str
        """
        self._face_set_name = face_set_name

    @property
    def face_set_capacity(self):
        r"""Gets the face_set_capacity of this CreateFaceSetReq.

        人脸库最大的容量，填写1万整数倍的数字，例如：30000。 默认为100000，最大值为100000，可通过创建新的人脸库进行扩容，每个用户可免费默认使用10个人脸库，每个人脸库容量为10万个人脸特征。如需扩容单个人脸库规模，请联系华为云客服确认扩容规模与价格。

        :return: The face_set_capacity of this CreateFaceSetReq.
        :rtype: int
        """
        return self._face_set_capacity

    @face_set_capacity.setter
    def face_set_capacity(self, face_set_capacity):
        r"""Sets the face_set_capacity of this CreateFaceSetReq.

        人脸库最大的容量，填写1万整数倍的数字，例如：30000。 默认为100000，最大值为100000，可通过创建新的人脸库进行扩容，每个用户可免费默认使用10个人脸库，每个人脸库容量为10万个人脸特征。如需扩容单个人脸库规模，请联系华为云客服确认扩容规模与价格。

        :param face_set_capacity: The face_set_capacity of this CreateFaceSetReq.
        :type face_set_capacity: int
        """
        self._face_set_capacity = face_set_capacity

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
        if not isinstance(other, CreateFaceSetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

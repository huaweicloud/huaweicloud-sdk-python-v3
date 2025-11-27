# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportOtherResourceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'file': 'file',
        'type': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'file': 'file',
        'type': 'type',
        'region_id': 'region_id'
    }

    def __init__(self, file=None, type=None, region_id=None):
        r"""ImportOtherResourceRequestBody

        The model defined in huaweicloud sdk

        :param file: **参数解释：** 上传的物理机/虚拟机/中间件设备下载模板excel（相关的设备信息）。 **约束限制：** 不涉及。 **取值范围：** 物理机/虚拟机/中间件设备下载模板excel（相关的设备信息）。 **默认取值：** 不涉及。
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param type: **参数解释：** 导入类型。 **约束限制：** 不涉及。 **取值范围：** - vm：虚拟机。 - PM：物理机。 - Middleware：中间件设备。 **默认取值：** 不涉及。
        :type type: str
        :param region_id: **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度在[0,64]之间。 **默认取值：** 不涉及。
        :type region_id: str
        """
        
        

        self._file = None
        self._type = None
        self._region_id = None
        self.discriminator = None

        self.file = file
        self.type = type
        self.region_id = region_id

    @property
    def file(self):
        r"""Gets the file of this ImportOtherResourceRequestBody.

        **参数解释：** 上传的物理机/虚拟机/中间件设备下载模板excel（相关的设备信息）。 **约束限制：** 不涉及。 **取值范围：** 物理机/虚拟机/中间件设备下载模板excel（相关的设备信息）。 **默认取值：** 不涉及。

        :return: The file of this ImportOtherResourceRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this ImportOtherResourceRequestBody.

        **参数解释：** 上传的物理机/虚拟机/中间件设备下载模板excel（相关的设备信息）。 **约束限制：** 不涉及。 **取值范围：** 物理机/虚拟机/中间件设备下载模板excel（相关的设备信息）。 **默认取值：** 不涉及。

        :param file: The file of this ImportOtherResourceRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def type(self):
        r"""Gets the type of this ImportOtherResourceRequestBody.

        **参数解释：** 导入类型。 **约束限制：** 不涉及。 **取值范围：** - vm：虚拟机。 - PM：物理机。 - Middleware：中间件设备。 **默认取值：** 不涉及。

        :return: The type of this ImportOtherResourceRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ImportOtherResourceRequestBody.

        **参数解释：** 导入类型。 **约束限制：** 不涉及。 **取值范围：** - vm：虚拟机。 - PM：物理机。 - Middleware：中间件设备。 **默认取值：** 不涉及。

        :param type: The type of this ImportOtherResourceRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def region_id(self):
        r"""Gets the region_id of this ImportOtherResourceRequestBody.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度在[0,64]之间。 **默认取值：** 不涉及。

        :return: The region_id of this ImportOtherResourceRequestBody.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ImportOtherResourceRequestBody.

        **参数解释：** 区域id。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度在[0,64]之间。 **默认取值：** 不涉及。

        :param region_id: The region_id of this ImportOtherResourceRequestBody.
        :type region_id: str
        """
        self._region_id = region_id

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImportOtherResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

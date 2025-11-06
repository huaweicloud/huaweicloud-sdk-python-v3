# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventForensicInfoImageBlockForensic:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'msg': 'str',
        'path': 'str',
        'image': 'str',
        'version': 'bool',
        'result': 'str',
        'time': 'str'
    }

    attribute_map = {
        'type': 'type',
        'msg': 'msg',
        'path': 'path',
        'image': 'image',
        'version': 'version',
        'result': 'result',
        'time': 'time'
    }

    def __init__(self, type=None, msg=None, path=None, image=None, version=None, result=None, time=None):
        r"""EventForensicInfoImageBlockForensic

        The model defined in huaweicloud sdk

        :param type: **参数解释**： 阻断类型 **取值范围**： 不涉及
        :type type: str
        :param msg: **参数解释**： 阻断原因 **取值范围**： 不涉及
        :type msg: str
        :param path: **参数解释**： 路径 **取值范围**： 不涉及
        :type path: str
        :param image: **参数解释**： 镜像名称 **取值范围**： 不涉及
        :type image: str
        :param version: **参数解释**： 镜像版本 **取值范围**： 不涉及
        :type version: bool
        :param result: **参数解释**： 阻断结果 **取值范围**： 不涉及
        :type result: str
        :param time: **参数解释**： 发生时间 **取值范围**： 不涉及
        :type time: str
        """
        
        

        self._type = None
        self._msg = None
        self._path = None
        self._image = None
        self._version = None
        self._result = None
        self._time = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if msg is not None:
            self.msg = msg
        if path is not None:
            self.path = path
        if image is not None:
            self.image = image
        if version is not None:
            self.version = version
        if result is not None:
            self.result = result
        if time is not None:
            self.time = time

    @property
    def type(self):
        r"""Gets the type of this EventForensicInfoImageBlockForensic.

        **参数解释**： 阻断类型 **取值范围**： 不涉及

        :return: The type of this EventForensicInfoImageBlockForensic.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EventForensicInfoImageBlockForensic.

        **参数解释**： 阻断类型 **取值范围**： 不涉及

        :param type: The type of this EventForensicInfoImageBlockForensic.
        :type type: str
        """
        self._type = type

    @property
    def msg(self):
        r"""Gets the msg of this EventForensicInfoImageBlockForensic.

        **参数解释**： 阻断原因 **取值范围**： 不涉及

        :return: The msg of this EventForensicInfoImageBlockForensic.
        :rtype: str
        """
        return self._msg

    @msg.setter
    def msg(self, msg):
        r"""Sets the msg of this EventForensicInfoImageBlockForensic.

        **参数解释**： 阻断原因 **取值范围**： 不涉及

        :param msg: The msg of this EventForensicInfoImageBlockForensic.
        :type msg: str
        """
        self._msg = msg

    @property
    def path(self):
        r"""Gets the path of this EventForensicInfoImageBlockForensic.

        **参数解释**： 路径 **取值范围**： 不涉及

        :return: The path of this EventForensicInfoImageBlockForensic.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this EventForensicInfoImageBlockForensic.

        **参数解释**： 路径 **取值范围**： 不涉及

        :param path: The path of this EventForensicInfoImageBlockForensic.
        :type path: str
        """
        self._path = path

    @property
    def image(self):
        r"""Gets the image of this EventForensicInfoImageBlockForensic.

        **参数解释**： 镜像名称 **取值范围**： 不涉及

        :return: The image of this EventForensicInfoImageBlockForensic.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this EventForensicInfoImageBlockForensic.

        **参数解释**： 镜像名称 **取值范围**： 不涉及

        :param image: The image of this EventForensicInfoImageBlockForensic.
        :type image: str
        """
        self._image = image

    @property
    def version(self):
        r"""Gets the version of this EventForensicInfoImageBlockForensic.

        **参数解释**： 镜像版本 **取值范围**： 不涉及

        :return: The version of this EventForensicInfoImageBlockForensic.
        :rtype: bool
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this EventForensicInfoImageBlockForensic.

        **参数解释**： 镜像版本 **取值范围**： 不涉及

        :param version: The version of this EventForensicInfoImageBlockForensic.
        :type version: bool
        """
        self._version = version

    @property
    def result(self):
        r"""Gets the result of this EventForensicInfoImageBlockForensic.

        **参数解释**： 阻断结果 **取值范围**： 不涉及

        :return: The result of this EventForensicInfoImageBlockForensic.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this EventForensicInfoImageBlockForensic.

        **参数解释**： 阻断结果 **取值范围**： 不涉及

        :param result: The result of this EventForensicInfoImageBlockForensic.
        :type result: str
        """
        self._result = result

    @property
    def time(self):
        r"""Gets the time of this EventForensicInfoImageBlockForensic.

        **参数解释**： 发生时间 **取值范围**： 不涉及

        :return: The time of this EventForensicInfoImageBlockForensic.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this EventForensicInfoImageBlockForensic.

        **参数解释**： 发生时间 **取值范围**： 不涉及

        :param time: The time of this EventForensicInfoImageBlockForensic.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, EventForensicInfoImageBlockForensic):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

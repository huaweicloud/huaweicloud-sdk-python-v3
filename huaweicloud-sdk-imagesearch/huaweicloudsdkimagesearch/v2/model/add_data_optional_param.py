# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddDataOptionalParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'do_det': 'bool',
        'box': 'str',
        'do_cls': 'bool',
        'category': 'int'
    }

    attribute_map = {
        'do_det': 'do_det',
        'box': 'box',
        'do_cls': 'do_cls',
        'category': 'category'
    }

    def __init__(self, do_det=None, box=None, do_cls=None, category=None):
        """AddDataOptionalParam

        The model defined in huaweicloud sdk

        :param do_det: 是否进行目标检测，默认为true。
        :type do_det: bool
        :param box: 目标矩形框坐标，如给定则不进行目标检测，直接使用该box作为目标。格式为“x1,y1,x2,y2”（无空格），x1/y1为目标左上角坐标，x2/y2为目标右下角坐标，具体要求如下： - 0 &lt;&#x3D; x1 &lt; x2 &lt;&#x3D; width，默认要求x2-x1 &gt;&#x3D; 15，具体可参考服务类型说明。 - 0 &lt;&#x3D; y1 &lt; y2 &lt;&#x3D; height，默认要求y2-y1 &gt;&#x3D; 15，具体可参考服务类型说明。
        :type box: str
        :param do_cls: 是否进行对象分类，默认为true。
        :type do_cls: bool
        :param category: 对象类目，如给定则不进行对象分类，直接使用该category作为类目。具体类目信息可参见对应的服务类型说明。
        :type category: int
        """
        
        

        self._do_det = None
        self._box = None
        self._do_cls = None
        self._category = None
        self.discriminator = None

        if do_det is not None:
            self.do_det = do_det
        if box is not None:
            self.box = box
        if do_cls is not None:
            self.do_cls = do_cls
        if category is not None:
            self.category = category

    @property
    def do_det(self):
        """Gets the do_det of this AddDataOptionalParam.

        是否进行目标检测，默认为true。

        :return: The do_det of this AddDataOptionalParam.
        :rtype: bool
        """
        return self._do_det

    @do_det.setter
    def do_det(self, do_det):
        """Sets the do_det of this AddDataOptionalParam.

        是否进行目标检测，默认为true。

        :param do_det: The do_det of this AddDataOptionalParam.
        :type do_det: bool
        """
        self._do_det = do_det

    @property
    def box(self):
        """Gets the box of this AddDataOptionalParam.

        目标矩形框坐标，如给定则不进行目标检测，直接使用该box作为目标。格式为“x1,y1,x2,y2”（无空格），x1/y1为目标左上角坐标，x2/y2为目标右下角坐标，具体要求如下： - 0 <= x1 < x2 <= width，默认要求x2-x1 >= 15，具体可参考服务类型说明。 - 0 <= y1 < y2 <= height，默认要求y2-y1 >= 15，具体可参考服务类型说明。

        :return: The box of this AddDataOptionalParam.
        :rtype: str
        """
        return self._box

    @box.setter
    def box(self, box):
        """Sets the box of this AddDataOptionalParam.

        目标矩形框坐标，如给定则不进行目标检测，直接使用该box作为目标。格式为“x1,y1,x2,y2”（无空格），x1/y1为目标左上角坐标，x2/y2为目标右下角坐标，具体要求如下： - 0 <= x1 < x2 <= width，默认要求x2-x1 >= 15，具体可参考服务类型说明。 - 0 <= y1 < y2 <= height，默认要求y2-y1 >= 15，具体可参考服务类型说明。

        :param box: The box of this AddDataOptionalParam.
        :type box: str
        """
        self._box = box

    @property
    def do_cls(self):
        """Gets the do_cls of this AddDataOptionalParam.

        是否进行对象分类，默认为true。

        :return: The do_cls of this AddDataOptionalParam.
        :rtype: bool
        """
        return self._do_cls

    @do_cls.setter
    def do_cls(self, do_cls):
        """Sets the do_cls of this AddDataOptionalParam.

        是否进行对象分类，默认为true。

        :param do_cls: The do_cls of this AddDataOptionalParam.
        :type do_cls: bool
        """
        self._do_cls = do_cls

    @property
    def category(self):
        """Gets the category of this AddDataOptionalParam.

        对象类目，如给定则不进行对象分类，直接使用该category作为类目。具体类目信息可参见对应的服务类型说明。

        :return: The category of this AddDataOptionalParam.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this AddDataOptionalParam.

        对象类目，如给定则不进行对象分类，直接使用该category作为类目。具体类目信息可参见对应的服务类型说明。

        :param category: The category of this AddDataOptionalParam.
        :type category: int
        """
        self._category = category

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
        if not isinstance(other, AddDataOptionalParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

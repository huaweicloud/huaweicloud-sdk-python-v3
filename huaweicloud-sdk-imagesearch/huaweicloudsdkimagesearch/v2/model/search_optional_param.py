# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchOptionalParam:

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
        'category': 'int',
        'collapse_key': 'str',
        'max_scan_num': 'int',
        'nprobe': 'int',
        'text_lang': 'str'
    }

    attribute_map = {
        'do_det': 'do_det',
        'box': 'box',
        'do_cls': 'do_cls',
        'category': 'category',
        'collapse_key': 'collapse_key',
        'max_scan_num': 'max_scan_num',
        'nprobe': 'nprobe',
        'text_lang': 'text_lang'
    }

    def __init__(self, do_det=None, box=None, do_cls=None, category=None, collapse_key=None, max_scan_num=None, nprobe=None, text_lang=None):
        r"""SearchOptionalParam

        The model defined in huaweicloud sdk

        :param do_det: 是否进行目标检测，默认为true。
        :type do_det: bool
        :param box: 目标矩形框坐标，如给定则不进行目标检测，直接使用该box作为目标。格式为“x1,y1,x2,y2”（无空格），x1/y1为目标左上角坐标，x2/y2为目标右下角坐标，具体要求如下： - 0 &lt;&#x3D; x1 &lt; x2 &lt;&#x3D; width，默认要求x2-x1 &gt;&#x3D; 15，具体可参考服务类型说明。 - 0 &lt;&#x3D; y1 &lt; y2 &lt;&#x3D; height，默认要求y2-y1 &gt;&#x3D; 15，具体可参考服务类型说明。
        :type box: str
        :param do_cls: 是否进行对象分类，默认为true。
        :type do_cls: bool
        :param category: 对象类目，如给定则不进行对象分类，直接使用该category作为类目。具体类目信息可参见对应的服务类型说明。
        :type category: int
        :param collapse_key: 去重标签名，必须为服务实例custom_tags中已存在的key。 - 如给定则会对该key下相同value的数据进行去重，仅保留得分最高的数据。 - 针对没有设置该标签的数据，会直接过滤。
        :type collapse_key: str
        :param max_scan_num: 扫描节点上限。值越大精度越高，查询速度变慢。默认值为10000。
        :type max_scan_num: int
        :param nprobe: 查询考察中心点的数目。值越大精度越高，查询速度变慢。默认值为100。
        :type nprobe: int
        :param text_lang: 文本字符串的语言类型枚举值。
        :type text_lang: str
        """
        
        

        self._do_det = None
        self._box = None
        self._do_cls = None
        self._category = None
        self._collapse_key = None
        self._max_scan_num = None
        self._nprobe = None
        self._text_lang = None
        self.discriminator = None

        if do_det is not None:
            self.do_det = do_det
        if box is not None:
            self.box = box
        if do_cls is not None:
            self.do_cls = do_cls
        if category is not None:
            self.category = category
        if collapse_key is not None:
            self.collapse_key = collapse_key
        if max_scan_num is not None:
            self.max_scan_num = max_scan_num
        if nprobe is not None:
            self.nprobe = nprobe
        if text_lang is not None:
            self.text_lang = text_lang

    @property
    def do_det(self):
        r"""Gets the do_det of this SearchOptionalParam.

        是否进行目标检测，默认为true。

        :return: The do_det of this SearchOptionalParam.
        :rtype: bool
        """
        return self._do_det

    @do_det.setter
    def do_det(self, do_det):
        r"""Sets the do_det of this SearchOptionalParam.

        是否进行目标检测，默认为true。

        :param do_det: The do_det of this SearchOptionalParam.
        :type do_det: bool
        """
        self._do_det = do_det

    @property
    def box(self):
        r"""Gets the box of this SearchOptionalParam.

        目标矩形框坐标，如给定则不进行目标检测，直接使用该box作为目标。格式为“x1,y1,x2,y2”（无空格），x1/y1为目标左上角坐标，x2/y2为目标右下角坐标，具体要求如下： - 0 <= x1 < x2 <= width，默认要求x2-x1 >= 15，具体可参考服务类型说明。 - 0 <= y1 < y2 <= height，默认要求y2-y1 >= 15，具体可参考服务类型说明。

        :return: The box of this SearchOptionalParam.
        :rtype: str
        """
        return self._box

    @box.setter
    def box(self, box):
        r"""Sets the box of this SearchOptionalParam.

        目标矩形框坐标，如给定则不进行目标检测，直接使用该box作为目标。格式为“x1,y1,x2,y2”（无空格），x1/y1为目标左上角坐标，x2/y2为目标右下角坐标，具体要求如下： - 0 <= x1 < x2 <= width，默认要求x2-x1 >= 15，具体可参考服务类型说明。 - 0 <= y1 < y2 <= height，默认要求y2-y1 >= 15，具体可参考服务类型说明。

        :param box: The box of this SearchOptionalParam.
        :type box: str
        """
        self._box = box

    @property
    def do_cls(self):
        r"""Gets the do_cls of this SearchOptionalParam.

        是否进行对象分类，默认为true。

        :return: The do_cls of this SearchOptionalParam.
        :rtype: bool
        """
        return self._do_cls

    @do_cls.setter
    def do_cls(self, do_cls):
        r"""Sets the do_cls of this SearchOptionalParam.

        是否进行对象分类，默认为true。

        :param do_cls: The do_cls of this SearchOptionalParam.
        :type do_cls: bool
        """
        self._do_cls = do_cls

    @property
    def category(self):
        r"""Gets the category of this SearchOptionalParam.

        对象类目，如给定则不进行对象分类，直接使用该category作为类目。具体类目信息可参见对应的服务类型说明。

        :return: The category of this SearchOptionalParam.
        :rtype: int
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this SearchOptionalParam.

        对象类目，如给定则不进行对象分类，直接使用该category作为类目。具体类目信息可参见对应的服务类型说明。

        :param category: The category of this SearchOptionalParam.
        :type category: int
        """
        self._category = category

    @property
    def collapse_key(self):
        r"""Gets the collapse_key of this SearchOptionalParam.

        去重标签名，必须为服务实例custom_tags中已存在的key。 - 如给定则会对该key下相同value的数据进行去重，仅保留得分最高的数据。 - 针对没有设置该标签的数据，会直接过滤。

        :return: The collapse_key of this SearchOptionalParam.
        :rtype: str
        """
        return self._collapse_key

    @collapse_key.setter
    def collapse_key(self, collapse_key):
        r"""Sets the collapse_key of this SearchOptionalParam.

        去重标签名，必须为服务实例custom_tags中已存在的key。 - 如给定则会对该key下相同value的数据进行去重，仅保留得分最高的数据。 - 针对没有设置该标签的数据，会直接过滤。

        :param collapse_key: The collapse_key of this SearchOptionalParam.
        :type collapse_key: str
        """
        self._collapse_key = collapse_key

    @property
    def max_scan_num(self):
        r"""Gets the max_scan_num of this SearchOptionalParam.

        扫描节点上限。值越大精度越高，查询速度变慢。默认值为10000。

        :return: The max_scan_num of this SearchOptionalParam.
        :rtype: int
        """
        return self._max_scan_num

    @max_scan_num.setter
    def max_scan_num(self, max_scan_num):
        r"""Sets the max_scan_num of this SearchOptionalParam.

        扫描节点上限。值越大精度越高，查询速度变慢。默认值为10000。

        :param max_scan_num: The max_scan_num of this SearchOptionalParam.
        :type max_scan_num: int
        """
        self._max_scan_num = max_scan_num

    @property
    def nprobe(self):
        r"""Gets the nprobe of this SearchOptionalParam.

        查询考察中心点的数目。值越大精度越高，查询速度变慢。默认值为100。

        :return: The nprobe of this SearchOptionalParam.
        :rtype: int
        """
        return self._nprobe

    @nprobe.setter
    def nprobe(self, nprobe):
        r"""Sets the nprobe of this SearchOptionalParam.

        查询考察中心点的数目。值越大精度越高，查询速度变慢。默认值为100。

        :param nprobe: The nprobe of this SearchOptionalParam.
        :type nprobe: int
        """
        self._nprobe = nprobe

    @property
    def text_lang(self):
        r"""Gets the text_lang of this SearchOptionalParam.

        文本字符串的语言类型枚举值。

        :return: The text_lang of this SearchOptionalParam.
        :rtype: str
        """
        return self._text_lang

    @text_lang.setter
    def text_lang(self, text_lang):
        r"""Sets the text_lang of this SearchOptionalParam.

        文本字符串的语言类型枚举值。

        :param text_lang: The text_lang of this SearchOptionalParam.
        :type text_lang: str
        """
        self._text_lang = text_lang

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
        if not isinstance(other, SearchOptionalParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateLigandSvgReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smiles': 'str',
        'scaffold': 'str',
        'size': 'int',
        'height': 'int',
        'width': 'int',
        'alerts': 'str',
        'ncols': 'int',
        'bgopacity': 'float',
        'bgcolor': 'str',
        'fgcolor': 'str',
        'ccolor': 'str',
        'ncolor': 'str',
        'ocolor': 'str'
    }

    attribute_map = {
        'smiles': 'smiles',
        'scaffold': 'scaffold',
        'size': 'size',
        'height': 'height',
        'width': 'width',
        'alerts': 'alerts',
        'ncols': 'ncols',
        'bgopacity': 'bgopacity',
        'bgcolor': 'bgcolor',
        'fgcolor': 'fgcolor',
        'ccolor': 'ccolor',
        'ncolor': 'ncolor',
        'ocolor': 'ocolor'
    }

    def __init__(self, smiles=None, scaffold=None, size=None, height=None, width=None, alerts=None, ncols=None, bgopacity=None, bgcolor=None, fgcolor=None, ccolor=None, ncolor=None, ocolor=None):
        """CreateLigandSvgReq

        The model defined in huaweicloud sdk

        :param smiles: 分子SMILES表达式
        :type smiles: str
        :param scaffold: 分子骨架smiles表达式
        :type scaffold: str
        :param size: 尺寸
        :type size: int
        :param height: svg高度
        :type height: int
        :param width: svg宽度
        :type width: int
        :param alerts: 高亮子结构编号
        :type alerts: str
        :param ncols: 显示的列数
        :type ncols: int
        :param bgopacity: 背景透明度
        :type bgopacity: float
        :param bgcolor: 背景颜色
        :type bgcolor: str
        :param fgcolor: 前景色
        :type fgcolor: str
        :param ccolor: 碳颜色
        :type ccolor: str
        :param ncolor: 氮颜色
        :type ncolor: str
        :param ocolor: 氧颜色
        :type ocolor: str
        """
        
        

        self._smiles = None
        self._scaffold = None
        self._size = None
        self._height = None
        self._width = None
        self._alerts = None
        self._ncols = None
        self._bgopacity = None
        self._bgcolor = None
        self._fgcolor = None
        self._ccolor = None
        self._ncolor = None
        self._ocolor = None
        self.discriminator = None

        self.smiles = smiles
        if scaffold is not None:
            self.scaffold = scaffold
        if size is not None:
            self.size = size
        if height is not None:
            self.height = height
        if width is not None:
            self.width = width
        if alerts is not None:
            self.alerts = alerts
        if ncols is not None:
            self.ncols = ncols
        if bgopacity is not None:
            self.bgopacity = bgopacity
        if bgcolor is not None:
            self.bgcolor = bgcolor
        if fgcolor is not None:
            self.fgcolor = fgcolor
        if ccolor is not None:
            self.ccolor = ccolor
        if ncolor is not None:
            self.ncolor = ncolor
        if ocolor is not None:
            self.ocolor = ocolor

    @property
    def smiles(self):
        """Gets the smiles of this CreateLigandSvgReq.

        分子SMILES表达式

        :return: The smiles of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._smiles

    @smiles.setter
    def smiles(self, smiles):
        """Sets the smiles of this CreateLigandSvgReq.

        分子SMILES表达式

        :param smiles: The smiles of this CreateLigandSvgReq.
        :type smiles: str
        """
        self._smiles = smiles

    @property
    def scaffold(self):
        """Gets the scaffold of this CreateLigandSvgReq.

        分子骨架smiles表达式

        :return: The scaffold of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._scaffold

    @scaffold.setter
    def scaffold(self, scaffold):
        """Sets the scaffold of this CreateLigandSvgReq.

        分子骨架smiles表达式

        :param scaffold: The scaffold of this CreateLigandSvgReq.
        :type scaffold: str
        """
        self._scaffold = scaffold

    @property
    def size(self):
        """Gets the size of this CreateLigandSvgReq.

        尺寸

        :return: The size of this CreateLigandSvgReq.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this CreateLigandSvgReq.

        尺寸

        :param size: The size of this CreateLigandSvgReq.
        :type size: int
        """
        self._size = size

    @property
    def height(self):
        """Gets the height of this CreateLigandSvgReq.

        svg高度

        :return: The height of this CreateLigandSvgReq.
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this CreateLigandSvgReq.

        svg高度

        :param height: The height of this CreateLigandSvgReq.
        :type height: int
        """
        self._height = height

    @property
    def width(self):
        """Gets the width of this CreateLigandSvgReq.

        svg宽度

        :return: The width of this CreateLigandSvgReq.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this CreateLigandSvgReq.

        svg宽度

        :param width: The width of this CreateLigandSvgReq.
        :type width: int
        """
        self._width = width

    @property
    def alerts(self):
        """Gets the alerts of this CreateLigandSvgReq.

        高亮子结构编号

        :return: The alerts of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._alerts

    @alerts.setter
    def alerts(self, alerts):
        """Sets the alerts of this CreateLigandSvgReq.

        高亮子结构编号

        :param alerts: The alerts of this CreateLigandSvgReq.
        :type alerts: str
        """
        self._alerts = alerts

    @property
    def ncols(self):
        """Gets the ncols of this CreateLigandSvgReq.

        显示的列数

        :return: The ncols of this CreateLigandSvgReq.
        :rtype: int
        """
        return self._ncols

    @ncols.setter
    def ncols(self, ncols):
        """Sets the ncols of this CreateLigandSvgReq.

        显示的列数

        :param ncols: The ncols of this CreateLigandSvgReq.
        :type ncols: int
        """
        self._ncols = ncols

    @property
    def bgopacity(self):
        """Gets the bgopacity of this CreateLigandSvgReq.

        背景透明度

        :return: The bgopacity of this CreateLigandSvgReq.
        :rtype: float
        """
        return self._bgopacity

    @bgopacity.setter
    def bgopacity(self, bgopacity):
        """Sets the bgopacity of this CreateLigandSvgReq.

        背景透明度

        :param bgopacity: The bgopacity of this CreateLigandSvgReq.
        :type bgopacity: float
        """
        self._bgopacity = bgopacity

    @property
    def bgcolor(self):
        """Gets the bgcolor of this CreateLigandSvgReq.

        背景颜色

        :return: The bgcolor of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._bgcolor

    @bgcolor.setter
    def bgcolor(self, bgcolor):
        """Sets the bgcolor of this CreateLigandSvgReq.

        背景颜色

        :param bgcolor: The bgcolor of this CreateLigandSvgReq.
        :type bgcolor: str
        """
        self._bgcolor = bgcolor

    @property
    def fgcolor(self):
        """Gets the fgcolor of this CreateLigandSvgReq.

        前景色

        :return: The fgcolor of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._fgcolor

    @fgcolor.setter
    def fgcolor(self, fgcolor):
        """Sets the fgcolor of this CreateLigandSvgReq.

        前景色

        :param fgcolor: The fgcolor of this CreateLigandSvgReq.
        :type fgcolor: str
        """
        self._fgcolor = fgcolor

    @property
    def ccolor(self):
        """Gets the ccolor of this CreateLigandSvgReq.

        碳颜色

        :return: The ccolor of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._ccolor

    @ccolor.setter
    def ccolor(self, ccolor):
        """Sets the ccolor of this CreateLigandSvgReq.

        碳颜色

        :param ccolor: The ccolor of this CreateLigandSvgReq.
        :type ccolor: str
        """
        self._ccolor = ccolor

    @property
    def ncolor(self):
        """Gets the ncolor of this CreateLigandSvgReq.

        氮颜色

        :return: The ncolor of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._ncolor

    @ncolor.setter
    def ncolor(self, ncolor):
        """Sets the ncolor of this CreateLigandSvgReq.

        氮颜色

        :param ncolor: The ncolor of this CreateLigandSvgReq.
        :type ncolor: str
        """
        self._ncolor = ncolor

    @property
    def ocolor(self):
        """Gets the ocolor of this CreateLigandSvgReq.

        氧颜色

        :return: The ocolor of this CreateLigandSvgReq.
        :rtype: str
        """
        return self._ocolor

    @ocolor.setter
    def ocolor(self, ocolor):
        """Sets the ocolor of this CreateLigandSvgReq.

        氧颜色

        :param ocolor: The ocolor of this CreateLigandSvgReq.
        :type ocolor: str
        """
        self._ocolor = ocolor

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
        if not isinstance(other, CreateLigandSvgReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
